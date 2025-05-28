import os

PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # Can be "openai" or "groq"

if PROVIDER == "groq":
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
elif PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_completion(messages, model="gpt-4", temperature=0.7):
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
