import psycopg2
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    conn = psycopg2.connect("host=yb-tserver-n1-europe port=5433 dbname=flight_db user=yugabyte password=yugabyte")

    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("SELECT * FROM airline")
    row = cur.fetchone()
    print(f"Query returned: {row[0]}, {row[1]}, {row[2]}")

    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')

    return config.make_wsgi_app()