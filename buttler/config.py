from pathlib import Path
import os

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    def __init__(self):
        self.jenkins_url = os.getenv("JENKINS_URL")
        self.jenkins_user = os.getenv("JENKINS_USER")
        self.jenkins_password = os.getenv("JENKINS_PASSWORD")


def get_config():
    return Config()
