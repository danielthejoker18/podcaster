import os
import json
import re
from utils.prompts import PROMPTS
from config import LANGUAGE
from llms.llm_provider import chat_completion

MODELO = os.getenv("MODELO", "llama-3.3-70b-versatile")

def plan_topic(theme: str, duration_minutes: int = 15, num_speakers: int = 2, language: str = LANGUAGE):
    prompt_template = PROMPTS["topic_planner"].get(language, PROMPTS["topic_planner"]["en"])
    prompt = prompt_template.format(theme=theme, duration=duration_minutes, speakers=num_speakers)

    response = chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful podcast planning assistant."},
            {"role": "user", "content": prompt}
        ],
        model=MODELO,  # ou mistral, dependendo do seu .env
        temperature=0.7
    )

    if response is None:
        print("❌ No response received from LLM.")
        return None

    try:
        content = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error accessing LLM response content: {e}")
        print(f"Raw response: {response}")
        return None

    cleaned = re.sub(r"^```(?:json)?\n?|```$", "", content.strip(), flags=re.MULTILINE)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        print("❌ Could not parse JSON. Raw cleaned response:")
        print(cleaned)
        return None

