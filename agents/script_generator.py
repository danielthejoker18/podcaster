import json
from config import LANGUAGE
from utils.prompts import PROMPTS
from llms.llm_provider import chat_completion

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
        model="gpt-4",
        temperature=0.8
    )
