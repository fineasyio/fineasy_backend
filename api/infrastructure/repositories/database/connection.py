import pymongo

from api.infrastructure.repositories.database.environment import DatabaseEnvironment


class DatabaseConnection:

    def __set_database_connection(self, collection: str):
        __client = pymongo.MongoClient(DatabaseEnvironment.get_connection_string(),
                                       serverSelectionTimeoutMS=5000)
        __database = __client[str(DatabaseEnvironment.db_name)][collection]
        return __database

    def connect(self, collection: str):
        try:
            return self.__set_database_connection(collection=collection)
        except Exception as exception:
            print(f"[ERROR] The data producer has an error: \n{exception}")