import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGPT_API_KEY")

response = requests.post(
    "https://togpt.ir/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "model": "gpt-5",
        "messages": [
            {
                "role": "user",
                "content": "Say hello in one short sentence."
            }
        ],
    },
)

print("Status:", response.status_code)
print("Body:", response.text)