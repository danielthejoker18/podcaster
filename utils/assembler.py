import os
import subprocess

from config import AUDIO_DIR

INPUT_LIST = os.path.join(AUDIO_DIR, "inputs.txt")
OUTPUT_FILE = os.path.join(AUDIO_DIR, "final_podcast.mp3")


def assemble_podcast():
    print("📦 Montando podcast final...")

    # Garante que o diretório existe
    if not os.path.exists(AUDIO_DIR):
        print("❌ Diretório de áudio não encontrado.")
        return

    # Lista e ordena os arquivos numericamente por prefixo
    audio_files = sorted([
        f for f in os.listdir(AUDIO_DIR)
        if f.endswith(".mp3") and f[0:2].isdigit()
    ], key=lambda x: int(x.split("_")[0]))

    if not audio_files:
        print("❌ Nenhum arquivo de áudio encontrado.")
        return

    with open(INPUT_LIST, "w", encoding="utf-8") as f:
        for filename in audio_files:
            full_path = os.path.abspath(os.path.join(AUDIO_DIR, filename))
            f.write(f"file '{full_path}'\n")

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

        # 🔥 Limpa os arquivos temporários, com verificação
        for filename in audio_files:
            try:
                os.remove(os.path.join(AUDIO_DIR, filename))
            except Exception as e:
                print(f"⚠️ Erro ao remover {filename}: {e}")

        try:
            os.remove(INPUT_LIST)
        except Exception as e:
            print(f"⚠️ Erro ao remover input list: {e}")

        print("🧹 Arquivos temporários removidos.")
    else:
        print("❌ Erro ao gerar podcast:")
        print(result.stderr)
