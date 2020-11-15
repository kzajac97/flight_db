CREATE TABLE airline (
    airline_id smallint PRIMARY KEY NOT NULL UNIQUE,
    name varchar NOT NULL UNIQUE,
    airline_code char(3) NOT NULL UNIQUE
);

CREATE TABLE airport (
    airport_id smallint PRIMARY KEY NOT NULL UNIQUE,
    airport_code char(3) NOT NULL UNIQUE,
    full_name varchar NOT NULL,
    origin_country varchar,
    origin_city varchar
);

CREATE TABLE route (
    route_id int PRIMARY KEY NOT NULL UNIQUE,
    departure_airport_id smallint NOT NULL,
    arrival_airport_id smallint NOT NULL,
    arrival_datetime date,
    departure_datetime date,

    CONSTRAINT departure_airport_fk
        FOREIGN KEY (departure_airport_id) REFERENCES airport(airport_id),

    CONSTRAINT arrival_airport_fk
        FOREIGN KEY (arrival_airport_id) REFERENCES airport(airport_id)
);


CREATE TABLE flight (
    flight_id int PRIMARY KEY NOT NULL UNIQUE,
    airline_id smallint NOT NULL,
    route_id int NOT NULL UNIQUE,
    flight_code char(12) NOT NULL UNIQUE,
    duration time,
    passengers smallint,
    intercontinental bit,

    CONSTRAINT airline_fk
        FOREIGN KEY (airline_id) REFERENCES airline(airline_id),

    CONSTRAINT route_fk
        FOREIGN KEY (route_id) REFERENCES route(route_id)
);
