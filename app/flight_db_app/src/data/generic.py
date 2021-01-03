from datetime import datetime as dt
from typing import List

from sqlalchemy.engine.result import ResultProxy


def convert_to_form_values(airlines: ResultProxy) -> List[dict]:
    """Convert ResultProxy from DB query into human-readable HTML form values"""
    return [{"name": name, "id": identifier} for identifier, name in tuple(airlines)]


def strip_data_time(timestamp: str) -> dt:
    return dt.strptime(timestamp, "%Y-%m-%d %H:%M")
