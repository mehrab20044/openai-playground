import os 

import requests 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGPT_API_KEY")

messages = []

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        print("Bye!")
        break

    if not user_input:
        continue

    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    # این بخش باید داخل while باشد
    response = requests.post(
        "https://togpt.ir/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "gpt-5",
            "messages": messages,
        },
    )

    response.raise_for_status()

    data = response.json()

    assistant_text = data["choices"][0]["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": assistant_text,
        }
    )

    print(f"AI: {assistant_text}")


    usage = data["usage"]

    print("Input tokens:", usage["prompt_tokens"])
    print("Output tokens:", usage["completion_tokens"])
    print("Total tokens:", usage["total_tokens"])
    print("Cost:", usage["cost"])