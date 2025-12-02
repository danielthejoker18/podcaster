import json
import re
import os
from config import LANGUAGE
from utils.prompts import PROMPTS
from llms.llm_provider import chat_completion

MODELO = os.getenv("MODELO", "deepseek-r1-distill-llama-70b")

def generate_script(section, speakers, style="casual", language=LANGUAGE):
    speaker_names = ", ".join(speakers)
    prompt_template = PROMPTS["script_generator"].get(language, PROMPTS["script_generator"]["en"])

    prompt = prompt_template.format(
        section_title=section["title"],
        section_description=section["description"],
        speaker_names=speaker_names,
        style=style
    )

    response = chat_completion(
        messages=[
            {"role": "system", "content": "You are a scriptwriter for a podcast."},
            {"role": "user", "content": prompt}
        ],
        model=MODELO,
        temperature=0.8
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown fencing if present
    # Remove Markdown code fences that may wrap the JSON response
    cleaned = re.sub(r'^```(?:json)?\n|```$', "", content.strip(), flags=re.MULTILINE)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        print(f"\n❌ Failed to parse JSON for section '{section['title']}'. Raw output:\n{cleaned}\n")
        return None
