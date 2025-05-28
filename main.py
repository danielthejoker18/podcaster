from agents.topic_planner import plan_topic
from agents.script_generator import generate_script
from agents.moderator import generate_moderation
from config import LANGUAGE

def main():
    theme = "AI in Healthcare"
    duration = 15
    speakers = ["Alice", "Bob"]
    style = "semi-formal"

    plan = plan_topic(theme, duration, len(speakers), LANGUAGE)
    sections = plan["sections"]

    moderation = generate_moderation(sections, speakers, style, LANGUAGE)

    full_script = []
    for section in sections:
        dialogue = generate_script(section, speakers, style, LANGUAGE)
        full_script.append({
            "section": section["title"],
            "dialogue": dialogue
        })

    # Print a preview
    print("INTRO:", moderation["intro"])
    for s in full_script:
        print(f"\n?? {s['section']}")
        for line in s["dialogue"]:
            print(f"{line['speaker']}: {line['text']}")
    print("\nOUTRO:", moderation["outro"])

if __name__ == "__main__":
    main()
