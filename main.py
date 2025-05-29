import os
from agents.topic_planner import plan_topic
from agents.script_generator import generate_script
from agents.moderator import generate_moderation
from utils.audio import generate_audio
from utils.assembler import assemble_podcast
from config import LANGUAGE
import json

def main():
    theme = "melhores placas de video para jogos em 2024"
    duration = 5
    speakers = ["dick", "sean"]
    style = "comedy"

    print(f"🎯 Tema: {theme}")
    plan = plan_topic(theme, duration, len(speakers), LANGUAGE)
    if not plan or not isinstance(plan, dict):
        print("❌ Invalid podcast plan received.")
        return

    sections = plan.get("sections", [])
    if not sections:
        print("❌ No sections found in plan.")
        return

    moderation = generate_moderation(sections, speakers, style, LANGUAGE)

    full_script = []

    print("\n🎙️ Geração de roteiro por seção...")
    for section in sections:
        dialogue = generate_script(section, speakers, style, LANGUAGE)
        if not dialogue or not isinstance(dialogue, list):
            print(f"⚠️ Skipping section '{section['title']}' due to invalid dialogue.")
            continue

        full_script.append({
            "section": section["title"],
            "dialogue": dialogue
        })

    # Preview no terminal
    print("\n🎧 Preview do episódio:\n")
    print("🎬 INTRO:", moderation["intro"])
    for s in full_script:
        print(f"\n🎯 {s['section']}")
        for line in s["dialogue"]:
            if isinstance(line, dict) and "speaker" in line and "text" in line:
                print(f"{line['speaker']}: {line['text']}")
            else:
                print(f"⚠️ Invalid dialogue line skipped: {line}")
    print("\n🏁 OUTRO:", moderation["outro"])

    # Geração de áudio
    print("\n🔊 Gerando áudios...")
    os.makedirs("output/audio", exist_ok=True)

    # Narrador (intro e outro)
    generate_audio(moderation["intro"], "output/audio/00_intro.mp3", speaker="narrator", lang=LANGUAGE)

    idx = 1
    for section in full_script:
        for i, line in enumerate(section["dialogue"]):
            if isinstance(line, dict) and "speaker" in line and "text" in line:
                filename = f"output/audio/{idx:02d}_{section['section'].replace(' ', '_')}_{i}_{line['speaker']}.mp3"
                generate_audio(line["text"], filename, speaker=line["speaker"], lang=LANGUAGE)
        idx += 1

    generate_audio(moderation["outro"], f"output/audio/{idx:02d}_outro.mp3", speaker="narrator", lang=LANGUAGE)

    print("✅ Áudios gerados com sucesso!")
    
    assemble_podcast()
    
    print("🎧 Podcast montado com sucesso!")

if __name__ == "__main__":
    main()
