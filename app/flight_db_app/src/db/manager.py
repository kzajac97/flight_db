import logging

from sqlalchemy import create_engine, text
from sqlalchemy import exc

from ..data import codes, generic, geo, tables
from . import insert, select, update


logger = logging.getLogger(__name__)


class TransactionManager:
    """Class responsible for all logic behind data base transactions"""
    connection_string = "postgresql+psycopg2://{user}:{password}@{server_ip}:{port}/{db_name}"
    success_message = "Completed Successfully"

    def __init__(self, db_config: dict):
        """
        :param db_config: configuration of YB t-server, should be read from config.ini file
        """
        self.db = create_engine(self.connection_string.format(
            user=db_config["db_user"],
            password=db_config["db_password"],
            server_ip=db_config["server_ip"],
            port=db_config["port"],
            db_name=db_config["db_name"],
        ))

        self.current_flight_id = self.query_flight_id() + 1
        self.current_route_id = self.query_route_id() + 1

    def register_flight(self, airline: int, departure: int, arrival: int):
        """
        Registers flight into database system
        Airline and Airport args must be database IDs!
        """
        airline = tables.airline_to_dict(self.query_airline_by_id(airline))
        departure = tables.airport_to_dict(self.query_airport_by_id(departure))
        arrival = tables.airport_to_dict(self.query_airport_by_id(arrival))
        flight_code = codes.create_flight_code(
            airline["code"], departure["code"], arrival["code"], self.query_flight_count(departure["id"], arrival["id"])
        )

        if departure["city"] == arrival["city"]:
            logger.error("Error! Arrival and departure locations are the same")
            return "Error! Arrival and departure locations must be different", ""

        with self.db.begin() as connection:
            try:
                connection.execute(text(insert.ROUTE.format(
                    route_id=self.current_route_id,
                    departure_id=departure["id"],
                    arrival_id=arrival["id"]
                )))

                connection.execute(text(insert.FLIGHT.format(
                    flight_id=self.current_flight_id,
                    airline_id=airline["id"],
                    route_id=self.current_route_id,
                    flight_code=flight_code,
                    flight_type=geo.is_intercontinental(departure["geo"], arrival["geo"])
                )))

                self.current_route_id += 1
                self.current_flight_id += 1

                logger.info("FLIGHT and ROUTE tables updated")
                return self.success_message, f"Flight Code is: {flight_code}"
            except exc.IntegrityError:
                logger.error("Unexpected Server Error!")
                return "Unexpected Server Error!", ""

    def report_flight(self, flight_code: str, passengers: str, departure_dt: str, arrival_dt: str) -> str:
        """Report flight into the database system"""
        try:
            departure_dt = generic.strip_data_time(departure_dt)
            arrival_dt = generic.strip_data_time(arrival_dt)
            duration = arrival_dt - departure_dt
        except ValueError:
            return "Error! Invalid datetime format"

        if arrival_dt < departure_dt:
            return "Error! Departure can't be after arrival"

        if int(passengers) > 500 or int(passengers) <= 0:
            return f"Error! Invalid number of passengers {passengers}!"

        try:
            flight = tables.flight_to_dict(self.query_flight_by_code(flight_code))
        except IndexError:
            return f"Error! Flight {flight_code} not found in database!"

        with self.db.begin() as connection:
            try:
                connection.execute(text(update.FLIGHT.format(
                    duration=str(duration),
                    passengers=passengers,
                    flight_code=flight_code
                )))

                connection.execute(text(update.ROUTE.format(
                    departure_dt=str(departure_dt),
                    arrival_dt=str(arrival_dt),
                    route_id=flight["route"],
                )))

                return self.success_message

            except exc.IntegrityError:
                logger.error("Unexpected Server Error!")
                return "Unexpected Server Error!"

    def register_airline(self, name: str, code: str) -> str:
        """Register airline into the database system"""
        with self.db.begin() as connection:
            try:
                connection.execute(text(insert.AIRLINE.format(name=name, code=code)))
                logger.info("AIRLINE table updated")
                return self.success_message
            except exc.IntegrityError:
                logger.error(f"Airline code not unique!\n{name} or {code} are already registered in database!")
                return f"Airline name and code must be unique!\n{name} or {code} are already registered in database!"

    def register_airport(self, code: str, name: str, country: str, city: str) -> str:
        """Register airport into the database system"""
        location = geo.get_geo_location(country)

        if len(code) != 3:
            logger.error("Invalid airport code!")
            return "Code must be 3 letters long!"

        with self.db.begin() as connection:
            try:
                connection.execute(text(insert.AIRPORT.format(
                    name=name, code=code.upper(), country=country, city=city, location=location,
                )))
                logger.info("AIRPORT table updated")
                return self.success_message
            except exc.IntegrityError:
                logger.error(f"Airport code {code.upper()} is already registered in FlightDB!")
                return f"Airport code {code.upper()} is already registered in FlightDB!"

    def query_airline_by_id(self, identifier: int):
        """Query for specific airline"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.AIRLINE_BY_ID.format(identifier)))

        return result

    def query_airport_by_id(self, identifier: int):
        """Query for specific airline"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.AIRPORT_BY_ID.format(identifier)))

        return result

    def query_all_airlines(self):
        """Query airlines in Database"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.AIRLINE_ID_AND_NAME))

        return result

    def query_all_airports(self):
        """Query airlines in Database"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.AIRPORT_ID_AND_NAME))

        return result

    def query_flight_by_code(self, flight_code: str):
        """Gets flight by its unique flight code"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.FLIGHT_BY_CODE.format(flight_code)))

        return result

    def query_route_by_id(self, route_id: str):
        """Gets route by its ID"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.ROUTE_BY_ID.format(route_id)))

        return result

    def query_route_id(self):
        """Gets current route ID value"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.MAX_ROUTE_ID))

        return int(tuple(result)[0][0])

    def query_flight_id(self):
        """Gets current flight ID value"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.MAX_FLIGHT_ID))

        return int(tuple(result)[0][0])

    def query_flight_count(self, departure, arrival) -> int:
        """Count number of flights between two airports"""
        with self.db.begin() as connection:
            result = connection.execute(text(select.FLIGHT_COUNT.format(departure_id=departure, arrival_id=arrival)))

        return int(tuple(result)[0][0])
