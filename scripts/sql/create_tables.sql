CREATE TABLE Airline (
    [AirlineId] [smallint] PRIMARY KEY NOT NULL UNIQUE,
    [Name] [varchar] NOT NULL UNIQUE
);

CREATE TABLE Airport (
    [AirportId] [smallint] PRIMARY KEY NOT NULL UNIQUE,
    [AirportCode] [char(3)] NOT NULL UNIQUE,
    [FullName] [varchar] NOT NULL,
    [OriginCountry] [varchar],
    [OriginCity] [varchar]
);

CREATE TABLE Route (
    [RouteId] [int] PRIMARY KEY NOT NULL UNIQUE,
    [ArrivalAirportId] [smallint] NOT NULL UNIQUE,
    [DepartureAirportId] [smallint] NOT NULL UNIQUE,
    [ArrivalDateTime] [date],
    [DepartureDateTime] [date],

    CONSTRAINT ArrivalAirportFk
        FOREIGN KEY (ArrivalAirportId) REFERENCES Airport(AirportId),

    CONSTRAINT DepartureAirportFk
        FOREIGN KEY (DepartureAirportId) REFERENCES Airport(AirportId)
);


CREATE TABLE Flight (
    [FlightId] [int] PRIMARY KEY NOT NULL UNIQUE,
    [AirportId] [smallint] NOT NULL UNIQUE,
    [RouteId] [int] NOT NULL UNIQUE,
    [FlightCode] [char(6)] NOT NULL UNIQUE,
    [Duration] [time],
    [Passengers] [smallint],
    [International] [bit],

    CONSTRAINT AirportFk
        FOREIGN KEY (AirportId) REFERENCES Airport(AirportId),

    CONSTRAINT RouteFk
        FOREIGN KEY (RouteId) REFERENCES Route(RouteId)
);
