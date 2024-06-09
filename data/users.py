import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class User:
    user_name: str
    user_password: str
    user_fullname: str


load_dotenv()
user_inn = os.getenv('INN')
user_password = os.getenv('PASS')

test_user = User(
    user_name=user_inn,
    user_password=user_password,
    user_fullname='АПОЛОНОВ ВАСИЛИЙ ВЯЧЕСЛАВОВИЧ'
)

