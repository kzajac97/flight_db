CREATE TABLE airline (
    airline_id smallint PRIMARY KEY NOT NULL UNIQUE,
    name varchar NOT NULL UNIQUE,
    airline_code char(3) NOT NULL UNIQUE
);


CREATE TABLE airport (
    airport_id smallint NULL,
    airport_code char(3) NOT NULL,
    full_name varchar NOT NULL,
    origin_country varchar,
    origin_city varchar,
    geographic_location varchar NOT NULL
) PARTITION BY LIST(geographic_location);

CREATE TABLE airports_europe
    PARTITION OF airport(
        airport_id,
        airport_code,
        full_name,
        origin_country,
        origin_city,
        geographic_location
) FOR VALUES IN ('Europe');

CREATE TABLE airports_america
    PARTITION OF airport(
        airport_id,
        airport_code,
        full_name,
        origin_country,
        origin_city,
        geographic_location
) FOR VALUES IN ('North America');
