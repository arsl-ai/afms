from dotenv import dotenv_values
from sqlalchemy.orm import DeclarativeBase
import os

config = {
	**dotenv_values(".env.shared"),  # load shared development variables
	**dotenv_values(".env.secret"),  # load sensitive variables
	**os.environ,  # override loaded values with environment variables
}
# print(config)

class Base(DeclarativeBase):
  pass