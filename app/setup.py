from setuptools import setup


requires = [
    "pyramid",
    "waitress",
]

setup(
    name="flight_db_app",
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = flight_db_app:main"
        ],
    },
)