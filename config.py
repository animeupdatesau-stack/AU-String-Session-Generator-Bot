from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "23639272"))
API_HASH = environ.get("API_HASH", "7d8f5d583048878a83071c5f267b059b")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7284759394")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1003460691511")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://amimeinhindi:n2PMMs07YTC1Unpg@cluster0.l6wffte.mongodb.net/?appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
