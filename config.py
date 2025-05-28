from dotenv import load_dotenv
import os
load_dotenv()

LANGUAGE = os.getenv("LANGUAGE", "en")