import os
from elevenlabs.client import ElevenLabs
from elevenlabs import Voice

# Pega chave da API do .env
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

if not ELEVEN_API_KEY:
    raise EnvironmentError("❌ ELEVEN_API_KEY não definida no .env.")

client = ElevenLabs(api_key=ELEVEN_API_KEY)

# Mapeamento de nomes para voice IDs
VOICE_ID_MAP = {
    "narrator": "EXAVITQu4vr4xnSDxMaL",  # Substitua por um ID real
    "dick": "TxGEqnHWrfWFTfGW9XjX",
    "sean": "pNInz6obpgDQGcFmaJgB",
}

def synthesize(text, output_path, lang="en", voice=None):
    voice_id = VOICE_ID_MAP.get(voice, voice)

    if voice_id is None:
        raise ValueError(f"❌ Voice not found for speaker '{voice}'.")

    audio_bytes = client.generate(
        text=text,
        voice=voice_id,
        model="eleven_multilingual_v2",  # ajuste conforme o necessário
        stream=False
    )

    # Salva o áudio em disco
    with open(output_path, "wb") as f:
        f.write(audio_bytes)
