

TOKEN = "6002621612:AAGEer6978KondtDdbf9F0N8xFqHB3xANOU"

ADMINS_IDS = []


POSTGRES_USER = "bot_user"
POSTGRES_PASSWORD = "Amina3261"
POSTGRES_DATABASE = "eat_time_db"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432


POSTGRES_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    name=POSTGRES_DATABASE
)