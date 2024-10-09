from dotenv import load_dotenv
import os 
from envparse import Env

env = Env()
load_dotenv()

class ConfigGpt: 
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    PROXY_USERNAME = os.environ.get("PROXY_USERNAME")
    PROXY_PASS = os.environ.get("PROXY_PASS") 
    PROXY_ENDPOINT = os.environ.get("PROXY_ENDPOINT") 