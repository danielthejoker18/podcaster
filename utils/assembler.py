import os
import subprocess

from config import AUDIO_DIR

INPUT_LIST = os.path.join(AUDIO_DIR, "inputs.txt")
OUTPUT_FILE = os.path.join(AUDIO_DIR, "final_podcast.mp3")


def assemble_podcast():
    print("📦 Montando podcast final...")

    # Gera a lista de arquivos .mp3 ordenados
    audio_files = sorted([
        f for f in os.listdir(AUDIO_DIR)
        if f.endswith(".mp3")
    ])

    if not audio_files:
        print("❌ Nenhum arquivo de áudio encontrado.")
        return

    with open(INPUT_LIST, "w") as f:
        for filename in audio_files:
            full_path = os.path.abspath(os.path.join(AUDIO_DIR, filename))
            f.write(f"file '{full_path}'\n")

    # Monta comando ffmpeg
    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", INPUT_LIST,
        "-c", "copy",
        OUTPUT_FILE
    ]

    print("🔧 Executando ffmpeg...")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ Podcast final gerado com sucesso: {OUTPUT_FILE}")

        # 🔥 Limpa os arquivos temporários
        for filename in audio_files:
            os.remove(os.path.join(AUDIO_DIR, filename))
        os.remove(INPUT_LIST)
        print("🧹 Arquivos temporários removidos.")
    else:
        print("❌ Erro ao gerar podcast:")
        print(result.stderr)
