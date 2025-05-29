import os
import json
import re
from utils.prompts import PROMPTS
from config import LANGUAGE
from llms.llm_provider import chat_completion

MODELO = os.getenv("MODELO", "deepseek-r1-distill-llama-70b")

def plan_topic(theme: str, duration_minutes: int = 15, num_speakers: int = 2, language: str = LANGUAGE):
    prompt_template = PROMPTS["topic_planner"].get(language, PROMPTS["topic_planner"]["en"])
    prompt = prompt_template.format(theme=theme, duration=duration_minutes, speakers=num_speakers)

    response = chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful podcast planning assistant."},
            {"role": "user", "content": prompt}
        ],
        model=MODELO,
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    try:
        plan = json.loads(content)
        # Sanity check to ensure keys exist
        if not isinstance(plan, dict) or "sections" not in plan or "summary" not in plan:
            raise ValueError("Missing 'summary' or 'sections' in plan.")
        return plan
    except (json.JSONDecodeError, ValueError) as e:
        print("❌ Could not parse JSON. Raw cleaned response:")
        print(content)
        return None
