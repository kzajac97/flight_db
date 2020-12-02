from configparser import ConfigParser

from pyramid.view import view_config, view_defaults

from flight_db_app.src.transactions import TransactionManager


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
        return {}

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

    @view_config(route_name="register_airline_input", renderer="../templates/register_airline.pt")
    def register_airline_input(self):
        airline_data = dict(self.request.POST)
        message = self.tm.register_airline(
            name=airline_data["airline_name_form"],
            code=airline_data["airline_code_form"]
        )

        return {"message": message}

    @view_config(route_name="register_airport_input", renderer="../templates/register_airport.pt")
    def register_airport_inout(self):
        print(dict(self.request.POST))

        return {"message": "Successfully Registered Airport"}
