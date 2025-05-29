from agents.topic_planner import plan_topic
from agents.script_generator import generate_script
from agents.moderator import generate_moderation
from config import LANGUAGE

def main():
    theme = "People who won't shut up"
    duration = 15
    speakers = ["dick", "sean"]
    style = "commedy"

    plan = plan_topic(theme, duration, len(speakers), LANGUAGE)
    if not plan or not isinstance(plan, dict):
        print("❌ Invalid podcast plan received.")
        return

    sections = plan["sections"]

    moderation = generate_moderation(sections, speakers, style, LANGUAGE)

    full_script = []
    for section in sections:
        dialogue = generate_script(section, speakers, style, LANGUAGE)
        if not dialogue or not isinstance(dialogue, list):
            print(f"⚠️ Skipping section '{section['title']}' due to invalid dialogue.")
            continue
        
        full_script.append({
            "section": section["title"],
            "dialogue": dialogue
        })

    # Print a preview
    print("INTRO:", moderation["intro"])
    for s in full_script:
        print(f"\n?? {s['section']}")
        for line in s["dialogue"]:
            if isinstance(line, dict) and "speaker" in line and "text" in line:
                print(f"{line['speaker']}: {line['text']}")
            else:
                print(f"⚠️ Invalid dialogue line skipped: {line}")
    print("\nOUTRO:", moderation["outro"])

if __name__ == "__main__":
    main()
