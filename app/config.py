from pydantic import BaseSettings
from dotenv import load_dotenv
from dotenv import dotenv_values

class Settings(BaseSettings):
	database_hostname: str
	database_port: str
	database_password: str
	database_name: str
	database_username: str
	secret_key: str
	algorithm: str
	access_token_expire_minutes: int


	class Config:
		env_file = f"C:/Users/frank/AppData/Local/Programs/Python/Python38/.env"
		

settings = Settings()

