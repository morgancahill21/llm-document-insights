from src.config import MOCK_MODE
from src.prompts import STRUCTURED_INSIGHTS_PROMPT
from src.schemas import DocumentInsights
import json

if not MOCK_MODE:
    from openai import OpenAI
    import os
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_structured_insights(document: str) -> DocumentInsights:
    if MOCK_MODE:
        # Return a simple mock
        return DocumentInsights(
            risks=[{"category": "Mock Risk", "description": "This is a mock risk"}],
            action_items=[{"action": "Mock Action", "owner": "N/A", "deadline": "N/A"}]
        )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "You are a precise corporate assistant."},
            {"role": "user", "content": STRUCTURED_INSIGHTS_PROMPT.format(document=document)}
        ],
        temperature=0
    )
    raw_output = response.output_text
    data = json.loads(raw_output)
    return DocumentInsights(**data)
