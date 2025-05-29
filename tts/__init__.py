from .gtts_provider import synthesize as synthesize_gtts
from .macos_provider import synthesize as synthesize_macos
from .coqui_provider import synthesize as synthesize_coqui
from .elevenlabs_provider import synthesize as synthesize_elevenlabs

import os

def get_tts_provider(provider_name):
    if provider_name == "gtts":
        return synthesize_gtts
    elif provider_name == "macos":
        return synthesize_macos
    elif provider_name == "coqui":
        return synthesize_coqui
    elif provider_name == "elevenlabs":
        return synthesize_elevenlabs
    else:
        raise ValueError(f"Unsupported TTS provider: {provider_name}")
