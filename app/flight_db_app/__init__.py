from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_chameleon")  # for .pt templates
    # all URL paths
    config.add_route("home", "/")
    config.add_route("register_flight", "/register_flight")
    config.add_route("report_flight", "/report_flight")
    config.add_route("flight_stats", "/flight_stats")
    config.add_route("register_airport", "/register_airport")
    config.add_route("register_airline", "/register_airline")
    # Path to directory with all static views
    config.add_static_view(name="static", path="flight_db_app:static")
    config.scan(".views")

    return config.make_wsgi_app()
