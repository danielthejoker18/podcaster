import pyttsx3

# Mapeamento de nomes amigáveis para os voice IDs do macOS (ajuste conforme seu sistema)
VOICE_ID_MAP = {
    "Reed (Português (Brasil))": "com.apple.eloquence.pt-BR.Reed",
    "Shelley (Português (Brasil))": "com.apple.eloquence.pt-BR.Shelley",
    "Daniel": "com.apple.voice.compact.en-GB.Daniel",
    "Samantha": "com.apple.voice.compact.en-US.Samantha",
    "Narrador": "com.apple.voice.compact.pt-BR.Luciana",  # Exemplo extra
}

def synthesize(text, output_path, lang="en", voice=None):
    engine = pyttsx3.init()
    voice_id = None

    if voice:
        voice_id = VOICE_ID_MAP.get(voice)
        if voice_id is None:
            print(f"⚠️ Voz '{voice}' não encontrada no mapeamento. Usando voz padrão.")
    else:
        print("🔈 Nenhuma voz especificada. Usando voz padrão.")

    if voice_id:
        engine.setProperty("voice", voice_id)

    engine.save_to_file(text, output_path)
    engine.runAndWait()
    engine.stop()
