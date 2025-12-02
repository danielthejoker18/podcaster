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
    
    cleaned_text = clean_text(text)
    kwargs = {"text": cleaned_text, "output_path": output_path, "lang": lang}

    if "voice" in sig.parameters:
        kwargs["voice"] = voice

    synthesize(**kwargs)

    # Trim silence using ffmpeg
    trim_silence(output_path)

def clean_text(text):
    # Remove trailing periods to avoid "ponto" pronunciation
    text = text.strip()
    if text.endswith("."):
        text = text[:-1]
    return text

def trim_silence(file_path):
    import subprocess
    
    temp_path = file_path.replace(".wav", "_temp.wav")
    
    # Filter to remove silence from start and end
    # silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak
    # areverse
    # silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak
    # areverse
    
    command = [
        "ffmpeg",
        "-y",
        "-i", file_path,
        "-af", "silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak,areverse,silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak,areverse",
        temp_path
    ]
    
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.replace(temp_path, file_path)
        # print(f"✂️ Silêncio removido: {file_path}")
    except subprocess.CalledProcessError:
        print(f"⚠️ Falha ao remover silêncio de {file_path}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
