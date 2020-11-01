CREATE TABLE Airline (
    [AirlineId] [smallint] PRIMARY KEY NOT NULL UNIQUE,
    [Name] [varchar] NOT NULL UNIQUE,
    [AirlineCode] [char(3)] NOT NULL UNIQUE
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
    [DepartureAirportId] [smallint] NOT NULL UNIQUE,
    [DepartureAirportId] [smallint] NOT NULL UNIQUE,
    [ArrivalDateTime] [date],
    [DepartureDateTime] [date],

    CONSTRAINT DepartureAirportFk
        FOREIGN KEY (DepartureAirportId) REFERENCES Airport(AirportId),

    CONSTRAINT ArrivalAirportFk
        FOREIGN KEY (ArrivalAirportId) REFERENCES Airport(AirportId)
);


CREATE TABLE Flight (
    [FlightId] [int] PRIMARY KEY NOT NULL UNIQUE,
    [AirlineId] [smallint] NOT NULL UNIQUE,
    [RouteId] [int] NOT NULL UNIQUE,
    [FlightCode] [char(12)] NOT NULL UNIQUE,
    [Duration] [time],
    [Passengers] [smallint],
    [Intercontinental] [bit],

    CONSTRAINT AirlineFk
        FOREIGN KEY (AirlineId) REFERENCES Airline(AirlineId),

    CONSTRAINT RouteFk
        FOREIGN KEY (RouteId) REFERENCES Route(RouteId)
);
