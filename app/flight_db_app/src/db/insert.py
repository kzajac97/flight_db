# inserting strings
AIRLINE = "INSERT INTO airline (name, airline_code) VALUES ('{name}', '{code}');"
AIRPORT = """
INSERT INTO airport
(airport_code, full_name, origin_country, origin_city, geographic_location)
VALUES ('{code}', '{name}', '{country}', '{city}', '{location}')
"""

