import sys
import json
from pathlib import Path
from src.ingest import load_document
from src.extract import extract_structured_insights
from src.summarize import generate_summary
from src.prompts import SUMMARY_PROMPT

def run_pipeline(doc_path: str):
    # Load document
    document = load_document(doc_path)

    # Generate executive summary
    summary = generate_summary(document)

    # Generate structured insights (risks and action items)
    insights = extract_structured_insights(document)

    # Render Markdown
    risks_md = "\n".join(
        f"- **{risk.category}**: {risk.description}"
        for risk in insights.risks
    )

    actions_md = "\n".join(
        f"- {item.action} (Owner: {item.owner or 'N/A'}, Deadline: {item.deadline or 'N/A'})"
        for item in insights.action_items
    )

    report_md = f"""
# Executive Summary
{summary}

# Risks
{risks_md}

# Action Items
{actions_md}
"""
    return report_md, insights

def save_outputs(report_md, insights, output_dir="reports"):
    Path(output_dir).mkdir(exist_ok=True)

    # Save Markdown
    md_path = Path(output_dir) / "latest_report.md"
    md_path.write_text(report_md, encoding="utf-8")
    print(f"Markdown report saved to {md_path}")

    # Save JSON
    json_path = Path(output_dir) / "latest_report.json"
    json_path.write_text(insights.model_dump_json(indent=2), encoding="utf-8")
    print(f"Structured JSON saved to {json_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <path_to_document>")
        sys.exit(1)

    doc_path = sys.argv[1]
    report_md, insights = run_pipeline(doc_path)
    save_outputs(report_md, insights)

    # print Markdown to terminal
    print(report_md)


