import pytest
import requests
import allure

# steps
# 1. install -> pip install python-dotenv
# 2. open .env file using load_dotenv function
# 3. then access the file data using os module

from dotenv import load_dotenv
import os


def test_update_req():
    load_dotenv()
    user_name = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(f"Username:{user_name}")
    print(f"Password:{password}")

