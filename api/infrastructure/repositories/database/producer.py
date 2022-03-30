from api.infrastructure.repositories.database.connection import DatabaseConnection


class DataProducer:

    def __init__(self, connection: DatabaseConnection) -> None:
        self.__database_connection = connection

    def produce(self, body: dict):
        connection = self.__database_connection.connect(collection="data")
        try:
            connection.insert_one(body)
        except Exception as exception: 
            print(f"[ERROR] The data producer has an error: \n{exception}")