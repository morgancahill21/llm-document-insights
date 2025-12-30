from src.config import MOCK_MODE
from src.prompts import SUMMARY_PROMPT

# import Open ai if want to use open ai, this is mock mode
# from openai import OpenAI
# import os

if not MOCK_MODE:
    from openai import OpenAI
    import os
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(document: str) -> str:
    if MOCK_MODE:
        return "This is a mock executive summary of the document."

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "You summarize documents for executives."},
            {"role": "user", "content": SUMMARY_PROMPT.format(document=document)}
        ],
        temperature=0.3
    )
    return response.output_text

