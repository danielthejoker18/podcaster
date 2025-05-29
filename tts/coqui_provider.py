import os
from TTS.api import TTS
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

# Caminho para o modelo (baixado automaticamente se necessário)
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

# Inicializa
tts = TTS(model_name=MODEL_NAME, progress_bar=False, gpu=False)

def synthesize(text, output_path, lang="pt", voice=None):
    print(f"🎤 [Coqui] Gerando áudio em {lang}: {output_path}")
    tts.tts_to_file(text=text, file_path=output_path, speaker_wav=None, language=lang)
