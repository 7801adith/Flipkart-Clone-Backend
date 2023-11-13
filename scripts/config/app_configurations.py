import configparser

config = configparser.ConfigParser()
config.read('conf/application.conf')

db_conf = configparser.ConfigParser()
db_conf.read('conf/db.conf')

api_base_service_url = "/fastapi/template"

# Log Configuration
LOG_LEVEL = config.get('LOG', 'log_level')
LOG_BASE_PATH = config.get('LOG', 'base_path')
LOG_FILE_NAME = LOG_BASE_PATH + config.get('LOG', 'file_name')
LOG_HANDLERS = config.get('LOG', 'handlers')
LOGGER_NAME = config.get('LOG', 'logger_name')

# Application Configuration
APP_HOST = config.get("APP", "application_host")
APP_PORT = int(config.get("APP", "application_port"))

# Mongo Configuration
MONGO_HOST = db_conf.get("MONGO", "mongo_host")
MONGO_PORT = db_conf.get("MONGO", "mongo_port")
MONGO_DB = db_conf.get("MONGO", "mongo_db")
