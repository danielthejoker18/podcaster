import os

PROVIDER = os.getenv("LLM_PROVIDER", "groq")  # Can be "openai" or "groq"
MODELO = os.getenv("MODELO", "llama-3.3-70b-versatile")  # Default model

if PROVIDER == "groq":
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
elif PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_completion(messages, model=MODELO, temperature=0.7):
    model = model or os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")

    if PROVIDER == "openai":
        return openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
    elif PROVIDER == "groq":
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
