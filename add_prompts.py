import json
import os

def load_library():
    if os.path.exists("prompt_library.json"):
        with open("prompt_library.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_library(library):
    with open("prompt_library.json", "w", encoding="utf-8") as file:
        json.dump(library, file, indent=2, ensure_ascii=False)
        print("✅ Prompt added successfully.")

def main():
    print("📚 Dueling Daemon Prompt Loader")

    prompt = input("\nEnter your philosophical prompt: ").strip()
    socratic = input("\n[⚖] Socratic Core response: ").strip()
    nietzschean = input("\n[🔥] Nietzschean Core response: ").strip()
    unified = input("\n[🧩] Unified Voice: ").strip()
    tags_input = input("\nTags (comma-separated): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

    new_entry = {
        "prompt": prompt,
        "socratic_core": socratic,
        "nietzschean_core": nietzschean,
        "unified_voice": unified,
        "tags": tags
    }

    library = load_library()
    library.append(new_entry)
    save_library(library)

if __name__ == "__main__":
    main()
