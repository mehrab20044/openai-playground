import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://togpt.ir/api/v1/chat/completions"
API_KEY = os.getenv("TOGPT_API_KEY")
MODEL = "gpt-5"

MAX_SESSION_COST = 0.01
MAX_REQUESTS = 5

session_cost = 0.0
request_count = 0

MAX_RETRIES = 3
MIN_REQUEST_INTERVAL = 1
last_request_time = 0.0

def wait_for_rate_limit():
    global last_request_time

    now = time.monotonic()
    elapsed = now - last_request_time

    if elapsed < MIN_REQUEST_INTERVAL:
        wait_time = MIN_REQUEST_INTERVAL - elapsed
        print(f"Rate limit: waiting {wait_time:.2f} seconds...")
        time.sleep(wait_time)

    last_request_time = time.monotonic()

def request_with_retry(messages):
    global session_cost, request_count
    for attempt in range(MAX_RETRIES):
        try:
            wait_for_rate_limit()
            if request_count >= MAX_REQUESTS:
                raise RuntimeError("Maximum request limit reached.")

            if session_cost >= MAX_SESSION_COST:
                raise RuntimeError("Maximum session cost reached.")

            request_count += 1
            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                },
                json={
                    "model": MODEL,
                    "messages": messages,
                },
                timeout=30,
            )

            if response.status_code == 200:
                data = response.json()

                request_cost = data["usage"].get("cost", 0.0)
                session_cost += request_cost

                print(f"Request cost: {request_cost}")
                print(f"Session cost: {session_cost:.6f}")
                print(f"Requests used: {request_count}/{MAX_REQUESTS}")

                return data

            if response.status_code in {429, 500, 502, 503, 504}:
                raise requests.RequestException(
                    f"Temporary API error: {response.status_code}"
                )

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Attempt {attempt + 1} failed: {error}")

            if attempt == MAX_RETRIES - 1:
                print("Max retries reached.")
                raise

            wait_time = 2 ** attempt

            print(f"Waiting {wait_time} seconds...")
            time.sleep(wait_time)

# messages = [
#     {
#         "role": "user",
#         "content": "در یک جمله کوتاه سلام کن."
#     }
# ]

# data = request_with_retry(messages)

# answer = data["choices"][0]["message"]["content"]

# print("AI:", answer)

messages_1 = [
    {
        "role": "user",
        "content": "در یک جمله کوتاه سلام کن."
    }
]

messages_2 = [
    {
        "role": "user",
        "content": "در یک جمله کوتاه خداحافظی کن."
    }
]
try:
    data_1 = request_with_retry(messages_1)
    answer_1 = data_1["choices"][0]["message"]["content"]
    print("AI 1:", answer_1)

    data_2 = request_with_retry(messages_2)
    answer_2 = data_2["choices"][0]["message"]["content"]
    print("AI 2:", answer_2)
except RuntimeError as error:
    print (f"Request blocked: {error}")

except requests.RequestException as error:
    print (f"API request failed after retries: {error}")