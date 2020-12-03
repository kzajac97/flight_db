from configparser import ConfigParser

from pyramid.view import view_config, view_defaults

from flight_db_app.src.db import TransactionManager
from flight_db_app.src.data.generic import convert_to_form_values


@view_defaults(renderer="../templates/home.pt")
class Views:
    def __init__(self, request):
        self.request = request
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.tm = TransactionManager(self.config["db_europe"])

    @view_config(route_name="home")
    def home(self):
        return {}

    @view_config(route_name="register_flight", renderer="../templates/register_flight.pt")
    def register_flight(self):
        airlines = self.tm.query_all_airlines()
        airports = self.tm.query_all_airports()

        return {
            "message": "",
            "airline_options": convert_to_form_values(airlines),
            "airport_options": convert_to_form_values(airports),
        }

    @view_config(route_name="report_flight", renderer="../templates/report_flight.pt")
    def report_flight(self):
        return {}

    @view_config(route_name="flight_stats", renderer="../templates/flight_stats.pt")
    def flight_stats(self):
        return {}

    @view_config(route_name="register_airport", renderer="../templates/register_airport.pt")
    def register_airport(self):
        return {"message": ""}

    @view_config(route_name="register_airline", renderer="../templates/register_airline.pt")
    def register_airline(self):
        return {"message": ""}

    @view_config(route_name="register_flight_input", renderer="../templates/register_flight.pt")
    def register_flight_input(self):
        airlines = self.tm.query_all_airlines()
        airports = self.tm.query_all_airports()

        form = dict(self.request.POST)
        message = self.tm.register_flight(
            airline=form["airline_id_select"],
            departure=form["departure_airport_id_select"],
            arrival=form["arrival_airport_id_select"],
        )

        return {
            "message": message,
            "airline_options": convert_to_form_values(airlines),
            "airport_options": convert_to_form_values(airports),
        }

    @view_config(route_name="register_airline_input", renderer="../templates/register_airline.pt")
    def register_airline_input(self):
        form = dict(self.request.POST)
        message = self.tm.register_airline(name=form["airline_name_form"], code=form["airline_code_form"])

        return {"message": message}

    @view_config(route_name="register_airport_input", renderer="../templates/register_airport.pt")
    def register_airport_inout(self):
        form = dict(self.request.POST)
        message = self.tm.register_airport(
            name=form["airport_full_name_form"],
            country=form["origin_country_list"],
            city=form["airport_origin_city_form"],
            code=form["airport_code_form"],
        )

        return {"message": message}
