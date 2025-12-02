# tts/gtts_provider.py

from gtts import gTTS

def synthesize(text, output_path, lang="en", voice=None):
    """
    Sintetiza texto usando Google Text-to-Speech (gTTS).
    O parâmetro `voice` é aceito, mas ignorado, pois gTTS não permite seleção de vozes específicas.
    """
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
    except Exception as e:
        print(f"❌ Erro ao gerar áudio com gTTS: {e}")
