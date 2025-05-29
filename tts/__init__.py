from .gtts_provider import synthesize as synthesize_gtts
from .macos_provider import synthesize as synthesize_macos
from .pyttsx3_provider import synthesize as synthesize_pyttsx3
from .elevenlabs_provider import synthesize as synthesize_elevenlabs

import os

def get_tts_provider(provider_name):
    if provider_name == "gtts":
        return synthesize_gtts
    elif provider_name == "macos":
        return synthesize_macos
    elif provider_name == "pyttsx3":
        return synthesize_pyttsx3
    elif provider_name == "elevenlabs":
        return synthesize_elevenlabs
    else:
        raise ValueError(f"Unsupported TTS provider: {provider_name}")
