"""Utility for obtaining the correct TTS synthesize function."""

def get_tts_provider(provider_name):
    """Return the synthesize function for the selected provider.

    Modules are imported lazily so that heavy dependencies are only required
    when the corresponding provider is actually used.
    """

    if provider_name == "gtts":
        from .gtts_provider import synthesize
        return synthesize
    elif provider_name == "macos":
        from .macos_provider import synthesize
        return synthesize
    elif provider_name == "coqui":
        from .coqui_provider import synthesize
        return synthesize
    elif provider_name == "elevenlabs":
        from .elevenlabs_provider import synthesize
        return synthesize
    else:
        raise ValueError(f"Unsupported TTS provider: {provider_name}")
