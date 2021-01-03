from pyramid.config import Configurator


def main(global_config, **settings):
    """Main function which returns WSGI application"""
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")  # for .pt templates
        config.include(".routes")
        config.scan(".views")

    return config.make_wsgi_app()
