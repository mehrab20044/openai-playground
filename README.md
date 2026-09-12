# OpenAI Playground

Learning project for Phase 2 - Week 4 of the AI Backend Playbook.

## complete

- Day 11 - LLM Fundamentals ✅
- Day 12 - Multi-turn Chat CLI + Token/Cost Tracking ✅
- Day 13 - Prompt Engineering + Evaluation Rubric ✅
- Day 14 - Prompt Comparison + Cost/Quality Analysis ✅
- Day 15 - Retry, Rate Limit and Cost Controls ✅

## Features

- LLM fundamentals glossary
- Tokenization experiments
- Multi-turn AI chat CLI
- Conversation history
- Token usage and cost tracking
- Five prompt strategies
- Repeated prompt experiments
- Raw experiment results
- Cost/quality comparison

## API Provider

The original Playbook uses the OpenAI API.

Because direct OpenAI API access was unavailable in the current environment, the practical API exercises were executed through ToGPT using an OpenAI-compatible API.

API keys are stored in `.env` and are excluded from Git.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install openai python-dotenv requests tiktoken
