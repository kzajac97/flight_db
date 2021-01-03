# inserting strings
AIRLINE = "INSERT INTO airline (name, airline_code) VALUES ('{name}', '{code}');"

AIRPORT = """
INSERT INTO airport
(airport_code, full_name, origin_country, origin_city, geographic_location)
VALUES ('{code}', '{name}', '{country}', '{city}', '{location}')
"""

FLIGHT = """
INSERT INTO flight
(flight_id, airline_id, route_id, flight_code, flight_type)
VALUES
({flight_id}, {airline_id}, {route_id}, '{flight_code}', '{flight_type}');
"""

ROUTE = """
INSERT INTO route
(route_id, departure_airport_id, arrival_airport_id)
VALUES
({route_id}, {departure_id}, {arrival_id});
"""

