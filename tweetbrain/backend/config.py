import json
import os

try:
    with open('secrets.json', 'r') as secrets_file:
        secrets = json.load(secrets_file)
except FileNotFoundError:
    secrets = os.environ

class Config:
    CONSUMER_KEY = secrets["CONSUMER_KEY"]
    CONSUMER_SECRET = secrets["CONSUMER_SECRET"]
    ACCESS_TOKEN = secrets["ACCESS_TOKEN"]
    ACCESS_SECRET = secrets["ACCESS_SECRET"]
