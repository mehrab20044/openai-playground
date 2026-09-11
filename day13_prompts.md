# Day 13 — Prompt Engineering

## Task
Classify backend errors into one of these categories:

- AUTH_ERROR
- DB_ERROR
- NETWORK_ERROR
- VALIDATION_ERROR
- UNKNOWN_ERROR

## Evaluation Rubric

Each prompt will be scored from 0 to 2 on:

1. Accuracy
   - آیا دسته‌بندی خطا درست است؟

2. Format
   - آیا فقط یکی از دسته‌های تعیین‌شده برمی‌گردد؟

3. Consistency
   - آیا برای ورودی مشابه، خروجی ثابت و قابل پیش‌بینی است؟

4. Instruction Following
   - آیا مدل دقیقاً قوانین Prompt را رعایت می‌کند؟

Maximum score: 8


## Prompt 1 — Baseline

خطای Backend زیر را در یکی از دسته‌های زیر قرار بده:

AUTH_ERROR
DB_ERROR
NETWORK_ERROR
VALIDATION_ERROR
UNKNOWN_ERROR

فقط نام دسته را برگردان.

ورودی:
Database connection timed out after 30 seconds


## Prompt 2 — Role Prompt

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



## Prompt 3 — Few-shot

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


## Prompt 4 — Structured Prompt

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