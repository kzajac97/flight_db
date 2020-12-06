import logging
import plotly
from configparser import ConfigParser

import pandas as pd
from pyramid.view import view_config, view_defaults

from flight_db_app.src.db import TransactionManager
from flight_db_app.src.data.generic import convert_to_form_values


logger = logging.getLogger(__name__)


@view_defaults(renderer="../templates/home.pt")
class Views:
    def __init__(self, request):
        self.request = request
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.tm = TransactionManager(self.config["db_europe"])

        logger.info("Running...")

    @view_config(route_name="home")
    def home(self):
        logger.info("Home")
        return {}

    @view_config(route_name="register_flight", renderer="../templates/register_flight.pt")
    def register_flight(self):
        logger.info("Register Flight")

        airlines = self.tm.query_all_airlines()
        airports = self.tm.query_all_airports()

        return {
            "message": "",
            "flight_code": "",
            "airline_options": convert_to_form_values(airlines),
            "airport_options": convert_to_form_values(airports),
        }

    @view_config(route_name="report_flight", renderer="../templates/report_flight.pt")
    def report_flight(self):
        logger.info("Report Flight")
        return {"message": ""}

    @view_config(route_name="flight_stats", renderer="../templates/flight_stats.pt")
    def flight_stats(self):
        logger.info("Flight Stats")
        airports = self.tm.query_all_airports()

        return {
            "airport_options": convert_to_form_values(airports),
        }

    @view_config(route_name="show_flight_input", renderer="../templates/stats.pt")
    def show_flight_stats(self):
        logger.info("Form submitted")
        form = dict(self.request.POST)

        stats = self.tm.query_all_airport_stats(form["airport_id_select"])

        sample_data = pd.DataFrame.from_records([["A", 10], ["B", 9], ["C", 8], ["D", 7], ["E", 6], ["F", 5], ["G", 4], ["H", 3], ["I", 1], ["K", 1]], columns=["name", "flights"])

        #with open(r"flight_db_app/templates/stats.pt", "r") as file:
        #    template = file.read()

        #fill_in = template.replace("#{top_arrivals}", sample_data.to_html(index=False, justify="center", classes="style-table"))

        #with open(r"flight_db_app/templates/show_stats.pt", "w") as file:
        #    file.write(fill_in)

        logger.info("Operation Completed")
        return {
            "airport": stats,
            "top_arrivals": sample_data,
        }

    @view_config(route_name="register_airport", renderer="../templates/register_airport.pt")
    def register_airport(self):
        logger.info("Flight Airport")
        return {"message": ""}

    @view_config(route_name="register_airline", renderer="../templates/register_airline.pt")
    def register_airline(self):
        logger.info("Register Airline")
        return {"message": ""}

    @view_config(route_name="register_flight_input", renderer="../templates/register_flight.pt")
    def register_flight_input(self):
        logger.info("Form submitted")

        airlines = self.tm.query_all_airlines()
        airports = self.tm.query_all_airports()

        form = dict(self.request.POST)
        message, code = self.tm.register_flight(
            airline=form["airline_id_select"],
            departure=form["departure_airport_id_select"],
            arrival=form["arrival_airport_id_select"],
        )

        logger.info("Operation Completed")
        return {
            "message": message,
            "flight_code": code,
            "airline_options": convert_to_form_values(airlines),
            "airport_options": convert_to_form_values(airports),
        }

    @view_config(route_name="report_flight_input", renderer="../templates/report_flight.pt")
    def report_flight_input(self):
        logger.info("Form submitted")
        form = dict(self.request.POST)
        message = self.tm.report_flight(
            flight_code=form["flight_code_form"],
            passengers=form["passengers_form"],
            departure_dt=form["departure_dt_form"],
            arrival_dt=form["arrival_dt_form"],
        )

        return {
            "message": message,
        }

    @view_config(route_name="register_airline_input", renderer="../templates/register_airline.pt")
    def register_airline_input(self):
        logger.info("Form submitted")
        form = dict(self.request.POST)
        message = self.tm.register_airline(name=form["airline_name_form"], code=form["airline_code_form"])
        logger.info("Operation Completed")

        return {"message": message}

    @view_config(route_name="register_airport_input", renderer="../templates/register_airport.pt")
    def register_airport_inout(self):
        logger.info("Form submitted")
        form = dict(self.request.POST)
        message = self.tm.register_airport(
            name=form["airport_full_name_form"],
            country=form["origin_country_list"],
            city=form["airport_origin_city_form"],
            code=form["airport_code_form"],
        )
        logger.info("Operation Completed")

        return {"message": message}
