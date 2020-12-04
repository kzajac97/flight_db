AIRLINE_BY_ID = "SELECT * FROM airline WHERE airline_id={};"
AIRPORT_BY_ID = "SELECT * FROM airport WHERE airport_id={};"
AIRLINE_ID_AND_NAME = "SELECT airline_id, name FROM airline;"
AIRPORT_ID_AND_NAME = "SELECT airport_id, full_name FROM airport;"
FLIGHT_BY_CODE = "SELECT * FROM flight WHERE flight_code='{}';"
ROUTE_BY_ID = "SELECT * FROM route WHERE route_id='{}';"
MAX_ROUTE_ID = "SELECT MAX(route_id) FROM route;"
MAX_FLIGHT_ID = "SELECT MAX(flight_id) FROM flight;"

FLIGHT_COUNT = """
SELECT COUNT(*)
FROM route
WHERE departure_airport_id={departure_id} AND arrival_airport_id={arrival_id};
"""
