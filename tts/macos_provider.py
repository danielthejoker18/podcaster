import os
# subprocess is unused; audio generation relies on the system 'say' command

VOICE_ID_MAP = {
    "Reed (Português (Brasil))": "com.apple.eloquence.pt-BR.Reed",
    "Shelley (Português (Brasil))": "com.apple.eloquence.pt-BR.Shelley",
    "Daniel": "com.apple.voice.compact.en-GB.Daniel",
    "Samantha": "com.apple.voice.compact.en-US.Samantha",
    "Narrador": "com.apple.voice.compact.pt-BR.Luciana",
}

def synthesize(text, output_path, lang="en", voice=None):
    if voice is None:
        voice = "Samantha"

    voice_id = VOICE_ID_MAP.get(voice, voice)
    if voice_id == voice:
        print(f"⚠️ Voz '{voice}' não mapeada explicitamente. Usando como está.")

    temp_path = output_path.replace(".mp3", ".aiff")

    # Gera o áudio .aiff
    command = f'say -v "{voice_id}" -o "{temp_path}" "{text}"'
    result = os.system(command)

    if result != 0:
        print(f"❌ Erro ao executar 'say' para a voz '{voice_id}'.")
        return

    # Converte para .mp3 com ffmpeg
    ffmpeg_command = f'ffmpeg -y -i "{temp_path}" "{output_path}" > /dev/null 2>&1'
    result = os.system(ffmpeg_command)

    if result != 0:
        print("❌ Erro ao converter áudio para mp3 usando ffmpeg.")

    # Remove arquivo temporário
    if os.path.exists(temp_path):
        os.remove(temp_path)
