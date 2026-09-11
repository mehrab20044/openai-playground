import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGPT_API_KEY")

API_URL = "https://togpt.ir/api/v1/chat/completions"
MODEL = "gpt-5"

prompts = {
    "baseline": """
خطای Backend زیر را در یکی از دسته‌های زیر قرار بده:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

فقط نام دسته را برگردان.

ورودی:
Database connection timed out after 30 seconds
""",

    "role": """
تو یک Senior Backend Developer هستی.

خطای Backend زیر را در یکی از دسته‌های زیر قرار بده:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

فقط نام دسته را برگردان.

ورودی:
Database connection timed out after 30 seconds
""",

    "few_shot": """
خطاهای Backend را فقط در یکی از دسته‌های زیر قرار بده:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

مثال‌ها:

ورودی:
Invalid password
خروجی:
AUTH_ERROR

ورودی:
PostgreSQL connection timeout
خروجی:
DB_ERROR

ورودی:
Request body is missing required field
خروجی:
VALIDATION_ERROR

حالا این خطا را دسته‌بندی کن:

ورودی:
Database connection timed out after 30 seconds

فقط نام دسته را برگردان.
""",

    "structured": """
خطای Backend زیر را بررسی و فقط یکی از دسته‌های زیر را انتخاب کن:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

قواعد:
- خطاهای Login، Password و Token → AUTH_ERROR
- خطاهای Database، SQL و Connection به DB → DB_ERROR
- خطاهای Network، DNS و اتصال بین سرویس‌ها → NETWORK_ERROR
- خطاهای ورودی نامعتبر یا ناقص → VALIDATION_ERROR
- اگر هیچ‌کدام نبود → UNKNOWN_ERROR

ورودی:
Database connection timed out after 30 seconds

فقط نام دسته را برگردان.
""",

    "combined": """
تو یک Senior Backend Developer هستی.

وظیفه:
خطای Backend را فقط در یکی از دسته‌های زیر قرار بده:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

قواعد:
- Login، Password و Token → AUTH_ERROR
- Database، SQL و DB Connection → DB_ERROR
- Network، DNS و Service Connection → NETWORK_ERROR
- ورودی ناقص یا نامعتبر → VALIDATION_ERROR
- اگر هیچ‌کدام نبود → UNKNOWN_ERROR

مثال‌ها:

ورودی:
Invalid password
خروجی:
AUTH_ERROR

ورودی:
PostgreSQL connection timeout
خروجی:
DB_ERROR

ورودی:
Missing required field
خروجی:
VALIDATION_ERROR

حالا این ورودی را دسته‌بندی کن:

Database connection timed out after 30 seconds

فقط نام دسته را برگردان.
"""
}


def run_prompt(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
    )

    if response.status_code != 200:
        print("Status:", response.status_code)
        print("Payload:", payload)
        print("Error body:", response.text)

    response.raise_for_status()

    data = response.json()

    output = data["choices"][0]["message"]["content"]
    usage = data["usage"]

    return {
        "output": output,
        "input_tokens": usage["prompt_tokens"],
        "output_tokens": usage["completion_tokens"],
        "total_tokens": usage["total_tokens"],
        "cost": usage["cost"],
    }  

results = []

for prompt_name, prompt_text in prompts.items():
    print(f"\nTesting: {prompt_name}")

    for run_number in range (1, 4):
        result = run_prompt(prompt_text)

        result["prompt_name"] = prompt_name
        result["run_number"] = run_number

        results.append(result)

        print(
            f"Run {run_number}: "
            f"output={result['output']} | "
            f"tokens={result['total_tokens']} | "
            f"cost={result['cost']}"    
        ) 

with open("day14_raw_results.json", "w", encoding="utf-8") as file:
    json.dump(
        results,
        file,
        ensure_ascii=False,
        indent=2,
    )

    print("\nRaw results saved to day14_raw_results.json")
