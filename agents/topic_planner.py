import os
import json
from utils.prompts import PROMPTS
from config import LANGUAGE
from llms.llm_provider import chat_completion

def plan_topic(theme: str, duration_minutes: int = 15, num_speakers: int = 2, language: str = LANGUAGE):
    prompt_template = PROMPTS["topic_planner"].get(language, PROMPTS["topic_planner"]["en"])
    prompt = prompt_template.format(theme=theme, duration=duration_minutes, speakers=num_speakers)

    response = chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful podcast planning assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4",
        temperature=0.7
    )

    content = response.choices[0].message["content"]
    
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("Warning: Could not parse response as JSON. Returning raw content.")
        return content
