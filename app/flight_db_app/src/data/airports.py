from typing import Optional


def get_geo_location(country: str) -> Optional[str]:
    """Converts country to location"""
    country_to_geo_location_mapping = {
        "Portugal": "Europe",
        "Spain": "Europe",
        "France": "Europe",
        "Italy": "Europe",
        "Malta": "Europe",
        "Switzerland": "Europe",
        "Austria": "Europe",
        "Slovenia": "Europe",
        "Croatia": "Europe",
        "Greece": "Europe",
        "Turkey": "Europe",
        "North Macedonia": "Europe",
        "Poland": "Europe",
        "Germany": "Europe",
        "Netherlands": "Europe",
        "Denmark": "Europe",
        "Sweden": "Europe",
        "Norway": "Europe",
        "Finland": "Europe",
        "Latvia": "Europe",
        "Russia": "Europe",
        "Belgium": "Europe",
        "Ireland": "Europe",
        "United Kingdom": "Europe",
        "Iceland": "Europe",
        "Canada": "North America",
        "Mexico": "North America",
        "United States": "North America",
    }

    return country_to_geo_location_mapping.get(country, None)
