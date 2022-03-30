from os.path import abspath, dirname
from os import environ
import dotenv


class Settings: 

    dotenv.load_dotenv(dotenv.find_dotenv())

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))
    
    @staticmethod
    def __get_env_var(env_var: str) -> str:
        env_var_value = environ.get(env_var)

        if not env_var_value:
            raise ValueError(f'{env_var} environment variable is missing!')

        return env_var_value

    @staticmethod
    def get_database_credentials() -> dict:
        credentials = {"DB_TYPE": Settings.__get_env_var('DB_TYPE'),
                       "DB_USER": Settings.__get_env_var('DB_USER'),
                       "DB_PASSWORD": Settings.__get_env_var('DB_PASSWORD'),
                       "DB_CLUSTER": Settings.__get_env_var('DB_CLUSTER'),
                       "DB_NAME": Settings.__get_env_var('DB_NAME')}

        return credentials
