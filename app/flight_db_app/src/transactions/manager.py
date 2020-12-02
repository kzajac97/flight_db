from sqlalchemy import create_engine, text
from sqlalchemy import exc


class TransactionManager:
    """Class responsible for all logic behind data base transactions"""
    connection_string = "postgresql+psycopg2://{user}:{password}@{server_ip}:{port}/{db_name}"
    success_message = "Completed Successfully"

    def __init__(self, db_config: dict):
        """
        :param db_config: configuration of YB t-server, should be read from config.ini file
        """
        self.db = create_engine(self.connection_string.format(
            user=db_config["db_user"],
            password=db_config["db_password"],
            server_ip=db_config["server_ip"],
            port=db_config["port"],
            db_name=db_config["db_name"],
        ))

        # insert strings
        self.insert_airline = "INSERT INTO airline (name, airline_code) VALUES ('{name}', '{code}');"

    def register_airline(self, name: str, code: str) -> str:
        """

        :param name:
        :param code:
        :return:
        """
        with self.db.begin() as connection:
            try:
                connection.execute(text(self.insert_airline.format(name=name, code=code)))
                return self.success_message
            except exc.IntegrityError:
                return f"Airline name and code must be unique!\n{name} or {code} are already registered in database!"
