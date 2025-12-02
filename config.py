from dotenv import load_dotenv
import os
load_dotenv(override=True)

LANGUAGE = os.getenv("LANGUAGE", "en")
TTS_PROVIDER = os.getenv("TTS_PROVIDER", "gtts")
AUDIO_DIR = os.getenv("AUDIO_DIR", "output/audio")