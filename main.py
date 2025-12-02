import os
from agents.topic_planner import plan_topic
from agents.script_generator import generate_script
from agents.moderator import generate_moderation
from utils.audio import generate_audio
from utils.assembler import assemble_podcast
from config import LANGUAGE

import argparse
import yaml
import sys

def load_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Config file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error parsing config file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="AI Podcaster Generator")
    parser.add_argument("--config", default="podcast_config.yaml", help="Path to configuration file")
    parser.add_argument("--theme", help="Override podcast theme")
    parser.add_argument("--duration", type=int, help="Override duration in minutes")
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Override with CLI args
    theme = args.theme if args.theme else config["episode"]["theme"]
    duration = args.duration if args.duration else config["episode"]["duration_minutes"]
    
    # Extract other settings
    language = config["podcast"].get("language", LANGUAGE)
    style = config["episode"]["style"]
    speakers_config = config["speakers"]
    speakers = [s["name"].lower() for s in speakers_config]

    # Identify Host
    host_name = speakers[0] # Default to first speaker
    for s in speakers_config:
        if s.get("role") == "host":
            host_name = s["name"]
            break
            
    print(f"🎙️  Host: {host_name}")

    print(f"🎯 Tema: {theme}")
    print(f"⏱️  Duração: {duration} min")
    print(f"🗣️  Speakers: {', '.join(speakers)}")
    
    plan = plan_topic(theme, duration, len(speakers), language)
    if not plan or not isinstance(plan, dict):
        print("❌ Invalid podcast plan received.")
        return

    sections = plan.get("sections", [])
    if not sections:
        print("❌ No sections found in plan.")
        return

    moderation = generate_moderation(sections, speakers, style, language, host_name=host_name)

    full_script = []

    print("\n🎙️ Geração de roteiro por seção...")
    for section in sections:
        dialogue = generate_script(section, speakers, style, language)
        if not dialogue or not isinstance(dialogue, list):
            print(f"⚠️ Skipping section '{section['title']}' due to invalid dialogue.")
            continue

        full_script.append({
            "section": section["title"],
            "dialogue": dialogue
        })

    # Preview no terminal
    print("\n🎧 Preview do episódio:\n")
    print(f"🎬 INTRO ({host_name}):", moderation["intro"])
    for s in full_script:
        print(f"\n🎯 {s['section']}")
        for line in s["dialogue"]:
            if isinstance(line, dict) and "speaker" in line and "text" in line:
                print(f"{line['speaker']}: {line['text']}")
            else:
                print(f"⚠️ Invalid dialogue line skipped: {line}")
    print(f"\n🏁 OUTRO ({host_name}):", moderation["outro"])

    # Geração de áudio
    print("\n🔊 Gerando áudios...")
    os.makedirs("output/audio", exist_ok=True)

    # Host (intro e outro)
    generate_audio(moderation["intro"], "output/audio/00_intro.wav", speaker=host_name, lang=language)

    idx = 1
    for section in full_script:
        section_title = section['section'].replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("é", "e")  # simplificação básica
        for i, line in enumerate(section["dialogue"]):
            if isinstance(line, dict) and "speaker" in line and "text" in line:
                speaker = line["speaker"].lower()
                filename = f"output/audio/{idx:02d}_{section_title}_{i}_{speaker}.wav"
                generate_audio(line["text"], filename, speaker=line["speaker"], lang=language)
        idx += 1

    generate_audio(moderation["outro"], f"output/audio/{idx:02d}_outro.wav", speaker=host_name, lang=language)

    print("✅ Áudios gerados com sucesso!")
    
    assemble_podcast()
    
    print("🎧 Podcast montado com sucesso!")

if __name__ == "__main__":
    main()
