import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY      = os.getenv("SECRET_KEY", "change-me")
ADMIN_USERNAME  = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD  = os.getenv("ADMIN_PASSWORD", "admin123")
