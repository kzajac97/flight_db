FLIGHT = """
UPDATE flight SET
duration='{duration}', passengers={passengers}
WHERE flight_code='{flight_code}';
"""

ROUTE = """
UPDATE route
SET departure_datetime='{departure_dt}', arrival_datetime='{arrival_dt}'
WHERE route_id={route_id};
"""
