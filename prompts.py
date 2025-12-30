SUMMARY_PROMPT = """
Provide a concise executive summary of the following document.
Focus on key objectives, decisions, and high-level takeaways.

Document:
{document}
"""

STRUCTURED_INSIGHTS_PROMPT = """
Analyze the following document and extract structured insights.

Return valid JSON with the following format:
{
  "risks": [
    {
      "category": "string",
      "description": "string"
    }
  ],
  "action_items": [
    {
      "action": "string",
      "owner": "string or null",
      "deadline": "string or null"
    }
  ]
}

Document:
{document}
"""
