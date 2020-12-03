from sqlalchemy.engine.result import ResultProxy


def airline_to_dict(query: ResultProxy) -> dict:
    """Convert ResultProxy for airline table into Python dictionary"""
    query = tuple(query)[0]
    return {"id": query[0], "name": query[1], "code": query[2]}


def airport_to_dict(query: ResultProxy) -> dict:
    """Convert ResultProxy for airport table into Python dictionary"""
    query = tuple(query)[0]
    return {"id": query[0], "code": query[1], "name": query[2], "country": query[3], "city": query[4], "geo": query[5]}
