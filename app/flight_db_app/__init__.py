from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_chameleon")  # for .pt templates
    # all URL paths
    config.add_route("home", "/")
    config.add_route("hello", "/howdy")
    # Path to directory with all static views
    config.add_static_view(name="static", path="flight_db_app:static")
    config.scan(".views")

    return config.make_wsgi_app()
