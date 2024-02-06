import os
from dotenv import load_dotenv

load_dotenv()


TESTING = True
DATABASE_URL=os.getenv('DATABASE_URL')
API_TITLE="Task Manager"
API_PREFIX = "/api/v1"
APP_DESPRICTION="api for task management service"
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
KEYCLOAK_CLIENT = os.getenv("KEYCLOAK_CLIENT")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
KEYCLOAK_ADMIN = os.getenv("KEYCLOAK_ADMIN")
KEYCLOAK_ADMIN_EMAIL = os.getenv("KEYCLOAK_ADMIN_EMAIL")
KEYCLOAK_ADMIN_PASSWORD = os.getenv("KEYCLOAK_ADMIN_PASSWORD")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
AUDIENCE = os.getenv("AUDIENCE")
ALGORITHM = os.getenv("ALGORITHM")