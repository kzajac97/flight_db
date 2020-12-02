from pyramid.view import (
    view_config,
    view_defaults
    )


@view_defaults(renderer="../templates/home.pt")
class Views:
    def __init__(self, request):
        self.request = request

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
        print(dict(self.request.POST))

        return {"message": "Successfully Registered Airline"}

    @view_config(route_name="register_airport_input", renderer="../templates/register_airport.pt")
    def register_airport_inout(self):
        print(dict(self.request.POST))

        return {"message": "Successfully Registered Airport"}
