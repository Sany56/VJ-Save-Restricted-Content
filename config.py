import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7613379908:AAGjbd72PxSuwf2H6I5uiul82jPeGnkATGg")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22654682"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c4bcd66081ef2f836d291604ffa8f5c1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://abinetolke80:<db_password>@cluster0.7qpb3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "abinetolke80")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
