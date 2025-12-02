import re

import os
import subprocess
from config import AUDIO_DIR

def get_sort_key(filename):
    # Extract section index (start) and line index (middle)
    # Expected format: 01_Title_0_speaker.wav
    # Or: 00_intro.wav (line index treated as -1 or 0)
    
    # Match section index (start of string)
    section_match = re.match(r"^(\d+)_", filename)
    section_idx = int(section_match.group(1)) if section_match else 999
    
    # Match line index (number between underscores before speaker/extension)
    # Looks for pattern like: _(\d+)_[a-zA-Z]+\.wav
    line_match = re.search(r"_(\d+)_[^_]+\.wav$", filename)
    line_idx = int(line_match.group(1)) if line_match else -1
    
    return (section_idx, line_idx)

INPUT_LIST = os.path.join(AUDIO_DIR, "inputs.txt")
OUTPUT_FILE = os.path.join(AUDIO_DIR, "final_podcast.mp3")

def assemble_podcast():
    print("📦 Montando podcast final...")

    # Garante que o diretório existe
    if not os.path.exists(AUDIO_DIR):
        print("❌ Diretório de áudio não encontrado.")
        return

    # Lista e ordena os arquivos numericamente por prefixo e índice de linha
    audio_files = sorted([
        f for f in os.listdir(AUDIO_DIR)
        if f.endswith(".wav") and f[0:2].isdigit()
    ], key=get_sort_key)

    print("📋 Ordem dos arquivos:")
    for f in audio_files:
        print(f"  - {f}")

    if not audio_files:
        print("❌ Nenhum arquivo de áudio encontrado.")
        return

    with open(INPUT_LIST, "w", encoding="utf-8") as f:
        for filename in audio_files:
            full_path = os.path.abspath(os.path.join(AUDIO_DIR, filename))
            f.write(f"file '{full_path}'\n")

    command = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", INPUT_LIST,
        "-c:a", "libmp3lame",
        "-b:a", "192k",
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
