def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    # all URL paths
    config.add_route("home", "/")
    config.add_route("register_flight", "/register_flight")
    config.add_route("report_flight", "/report_flight")
    config.add_route("flight_stats", "/flight_stats")
    config.add_route("register_airport", "/register_airport")
    config.add_route("register_airline", "/register_airline")
    config.add_route("register_airline_input", "/register_airline_input")
    config.add_route("register_airport_input", "/register_airport_input")
    config.add_route("register_flight_input", "/register_flight_input")
    config.add_route("report_flight_input", "/report_flight_input")
    config.add_route("show_flight_input", "/show_flight_input")
