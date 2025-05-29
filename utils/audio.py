import os
import json
from tts import get_tts_provider
import inspect

# Carrega o nome do provider e o mapeamento de vozes
TTS_PROVIDER = os.getenv("TTS_PROVIDER", "macos")
VOICE_MAP_RAW = os.getenv("VOICE_MAP", "{}")

try:
    VOICE_MAP = json.loads(VOICE_MAP_RAW)
except json.JSONDecodeError:
    print(f"⚠️ Erro ao decodificar VOICE_MAP: {VOICE_MAP_RAW}")
    VOICE_MAP = {}

def generate_audio(text, output_path, speaker=None, lang="en"):
    synthesize = get_tts_provider(TTS_PROVIDER)

    # Obtém a voz correspondente ao speaker, se fornecido
    voice = VOICE_MAP.get(speaker.lower(), None) if speaker else None

    # Verifica se a função aceita o argumento 'voice'
    sig = inspect.signature(synthesize)
    kwargs = {"text": text, "output_path": output_path, "lang": lang}

    if "voice" in sig.parameters:
        kwargs["voice"] = voice

    synthesize(**kwargs)
