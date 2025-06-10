import json

def main():
    try:
        with open("prompt_library.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)
    except FileNotFoundError:
        print("Error: prompt_library.json not found.")
        return

    user_input = input("Enter your philosophical prompt: ").strip().lower()

    found = False
    for item in prompts:
        if user_input in item["prompt"].lower():
            print("\n[⚖ Socratic Core]:")
            print(item["socratic_core"])
            print("\n[🔥 Nietzschean Core]:")
            print(item["nietzschean_core"])
            print("\n[🧩 Unified Voice]:")
            print(item["unified_voice"])
            found = True
            break

    if not found:
        print("\n🕳️ Prompt not found. Try a different question.")

if __name__ == "__main__":
    main()
