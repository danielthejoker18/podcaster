import json
import os
from config import LANGUAGE
from utils.prompts import PROMPTS
from llms.llm_provider import chat_completion

MODELO = os.getenv("MODELO", "deepseek-r1-distill-llama-70b")

def generate_moderation(sections, speakers, style="friendly", language=LANGUAGE, host_name="Host"):
    section_titles = [s["title"] for s in sections]
    speaker_names = ", ".join(speakers)

    prompt_template = PROMPTS["moderator"].get(language, PROMPTS["moderator"]["en"])
    prompt = prompt_template.format(
        sections=", ".join(section_titles),
        speaker_names=speaker_names,
        style=style,
        host_name=host_name
    )

    response = chat_completion(
        messages=[
            {"role": "system", "content": "You are a podcast narrator and moderator."},
            {"role": "user", "content": prompt}
        ],
        model=MODELO,
        temperature=0.7
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("Warning: Could not parse moderation response as JSON. Returning raw content.")
        return content
