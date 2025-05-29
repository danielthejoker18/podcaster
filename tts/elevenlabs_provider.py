import os
from elevenlabs.client import ElevenLabs

# Carrega a chave da API
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
if not ELEVEN_API_KEY:
    raise EnvironmentError("❌ ELEVEN_API_KEY não definida no .env.")

# Inicializa cliente
client = ElevenLabs(api_key=ELEVEN_API_KEY)

VOICE_ID_MAP = {
    "narrator": "EXAVITQu4vr4xnSDxMaL",  # Sarah
    "dick": "FGY2WhTYpPnrIDTdsKH5",      # Laura
    "sean": "IKne3meq5aSn9XLyUdCD",      # Charlie
    "george": "JBFqnCBsd6RMkjVDRZzb",    # George
    "callum": "N2lVS1w4EtoT3dr4eOWO",    # Callum
    "aria": "9BWtsMINqrJLrRacOk9x",      # Aria
}

def synthesize(text, output_path, lang="en", voice=None):
    if not voice:
        raise ValueError("❌ Nenhuma voz especificada para ElevenLabs.")

    voice_id = VOICE_ID_MAP.get(voice.lower())
    if not voice_id:
        raise ValueError(f"❌ Voz '{voice}' não encontrada no mapeamento de vozes.")

    audio_stream = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        text=text,
        output_format="mp3_44100_128"
    )

    # Salva o áudio iterando sobre o stream
    with open(output_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
