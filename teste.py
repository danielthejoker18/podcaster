import torch
from torch.serialization import safe_globals
from TTS.api import TTS

# Importações necessárias para deserializar o modelo xtts corretamente
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsArgs, XttsAudioConfig
from TTS.config.shared_configs import BaseDatasetConfig

# Usa o contexto seguro e permite as classes necessárias
with safe_globals({
    XttsConfig,
    XttsArgs,
    XttsAudioConfig,
    BaseDatasetConfig,
}):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

    print("🔊 Vozes disponíveis:", tts.speakers)

    tts.tts_to_file(
        text="Este é um teste com o modelo Coqui XTTS versão dois.",
        speaker=tts.speakers[0],
        language="pt",
        file_path="output_coqui.mp3"
    )
