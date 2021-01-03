def create_flight_code(airline: str, departure: str, arrival: str, counter: int) -> str:
    """Creates unique flight code"""
    return (airline + f"{counter:03d}" + departure + arrival).upper()
