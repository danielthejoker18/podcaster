import os
from TTS.api import TTS
try:
    from torch.serialization import add_safe_globals
    # Adiciona todas as classes necessárias como globais confiáveis
    from TTS.tts.configs.xtts_config import XttsConfig
    from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
    from TTS.config.shared_configs import BaseDatasetConfig

    add_safe_globals([
        XttsConfig,
        XttsAudioConfig,
        XttsArgs,
        BaseDatasetConfig,
    ])
except ImportError:
    pass

# Caminho para o modelo (baixado automaticamente se necessário)
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

# Inicializa
tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)

def synthesize(text, output_path, lang="pt", voice=None):
    print(f"🎤 [Coqui] Gerando áudio em {lang}: {output_path}")
    
    speaker_wav = "audio/silent.mp3"
    if voice:
        if os.path.exists(voice):
            speaker_wav = voice
            print(f"  🗣️ Usando voz de referência: {voice}")
        else:
            print(f"  ⚠️ Arquivo de voz não encontrado: {voice}. Usando silent.mp3.")
    else:
        print("  ⚠️ Nenhuma voz especificada. Usando silent.mp3.")

    try:
        tts.tts_to_file(text=text, file_path=output_path, speaker_wav=speaker_wav, language=lang)
    except Exception as e:
        print(f"  ❌ Erro ao gerar áudio: {e}")
