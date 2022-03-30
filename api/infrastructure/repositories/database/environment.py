from api.core.config import settings


class DatabaseEnvironment: 

    def __init__(self) -> None:
        self.__db_credentials: dict = settings.get_database_credentials()
        self.db_name = None
    
    @property
    def db_name(self):
        return self.__db_credentials["DB_NAME"]

    def get_connection_string(self) -> str:
        __connection_string = "{}://{}:{}@{}/{}?retryWrites=true&w=majority"
        return __connection_string.format(self.__db_credentials["DB_TYPE"],
                                        self.__db_credentials["DB_USER"],
                                        self.__db_credentials["DB_PASSWORD"],
                                        self.__db_credentials["DB_CLUSTER"],
                                        self.db_name)
