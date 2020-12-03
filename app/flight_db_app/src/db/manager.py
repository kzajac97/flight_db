from sqlalchemy import create_engine, text
from sqlalchemy import exc

from ..data import airports


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

        # insert strings
        self._insert_airline = "INSERT INTO airline (name, airline_code) VALUES ('{name}', '{code}');"
        self._insert_airport = """INSERT INTO airport
            (airport_code, full_name, origin_country, origin_city, geographic_location)
            VALUES ('{code}', '{name}', '{country}', '{city}', '{location}');"""

        # query strings
        self._select_airlines = "SELECT airline_id, name FROM airline;"

    def register_airline(self, name: str, code: str) -> str:
        """Register airline into the database system"""
        with self.db.begin() as connection:
            try:
                connection.execute(text(self._insert_airline.format(name=name, code=code)))
                return self.success_message
            except exc.IntegrityError:
                return f"Airline name and code must be unique!\n{name} or {code} are already registered in database!"

    def register_airport(self, code: str, name: str, country: str, city: str) -> str:
        """Register airport into the database system"""
        location = airports.get_geo_location(country)
        if len(code) != 3:
            return "Code must be 3 letters long!"

        with self.db.begin() as connection:
            try:
                connection.execute(text(self._insert_airport.format(
                    name=name, code=code.upper(), country=country, city=city, location=location,
                )))
                return self.success_message
            except exc.IntegrityError:
                return f"Airport code {code.upper()} is already registered in FlightDB!"

    def query_airlines(self):
        """Query airlines in Database"""
        with self.db.begin() as connection:
            result = connection.execute(text(self._select_airlines))

        return result
