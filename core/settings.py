class EnvData():
    project_title = 'Lavka_Delivery'
    pg_server = 'localhost'
    pg_user = 'root'
    pg_password = 'root'
    pg_database = 'lavka_app_db'
    secret = 'jd9034th54t7g8f73hd0923jd[0349jtp7hg67fb8c43bv784h'
    SQLAlchemy_DB_URL = (
        f'postgresql://{pg_user}:{pg_password}@{pg_server}/{pg_database}'
    )
    ver_prefix = '/v1'
    server_host = 'http://127.0.0.1:8000'


env_data = EnvData()


class Settings():
    ACCESS_TOKEN_VALIDITY_MINUTES: int = 60
    USERS_OPEN_REGISTRATION = True

    class Config:
        case_sensitive = True
        env_file = '.env'
