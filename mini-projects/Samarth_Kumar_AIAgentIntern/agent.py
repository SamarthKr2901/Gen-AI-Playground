"""
AI Application Screening Agent
Vriddhikar Society — AI Agent Development Intern Assignment
Author: Samarth Kumar

This script demonstrates the core AI processing step of the workflow.
It reads an applicant's details, sends them to Claude AI for screening,
and prints the structured result.

Usage:
    python agent.py

Requirements:
    pip install anthropic python-dotenv
    Add your key to the .env file: ANTHROPIC_API_KEY=your_key_here
"""

import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()  # loads ANTHROPIC_API_KEY from .env file automatically

# ── Configuration ──────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an HR screening assistant for Vriddhikar Society, a non-profit
focused on transforming education in India. You evaluate volunteer and internship
applications fairly and concisely. You always respond in valid JSON format only."""

SCREENING_PROMPT_TEMPLATE = """Review the following volunteer/internship application for Vriddhikar Society.

Role Applied For: {role}

Application Details:
{application_text}

Evaluate the candidate and respond ONLY with a JSON object in this exact format:
{{
  "score": <integer from 1 to 10>,
  "strengths": "<2-3 sentence summary of the candidate's relevant strengths>",
  "gaps": "<1-2 sentence summary of any missing qualifications or concerns>",
  "recommendation": "<one of: Shortlist / Hold / Reject>",
  "one_line_summary": "<a single sentence summary for the HR digest>"
}}

Scoring guide:
- 8-10: Strong fit, clear motivation, relevant skills → Shortlist
- 5-7:  Moderate fit, some relevant skills → Hold for review
- 1-4:  Poor fit, unclear motivation, missing key requirements → Reject"""

ACKNOWLEDGEMENT_PROMPT_TEMPLATE = """Write a short, warm, professional email to {name} confirming that
Vriddhikar Society has received their application for the {role} position.
Mention they will hear back within 5-7 business days.
Keep it under 80 words. Do not make promises about selection."""


# ── Core Functions ─────────────────────────────────────────────────────────────

def screen_application(client: anthropic.Anthropic, application: dict) -> dict:
    """
    Send an application to Claude for AI screening.
    Returns a dict with score, strengths, gaps, recommendation, summary.
    """
    prompt = SCREENING_PROMPT_TEMPLATE.format(
        role=application["role"],
        application_text=(
            f"Name: {application['name']}\n"
            f"Background: {application['background']}\n"
            f"Skills: {application['skills']}\n"
            f"Motivation: {application['motivation']}"
        )
    )

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Fast and cost-effective for screening
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    return json.loads(raw)


def generate_acknowledgement(client: anthropic.Anthropic, name: str, role: str) -> str:
    """
    Generate an auto-reply acknowledgement email for the applicant.
    """
    prompt = ACKNOWLEDGEMENT_PROMPT_TEMPLATE.format(name=name, role=role)

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()


def print_result(application: dict, result: dict, email: str):
    """Pretty-print the screening result to the console."""
    score = result["score"]
    rec = result["recommendation"]

    # Color-code recommendation
    colors = {"Shortlist": "\033[92m", "Hold": "\033[93m", "Reject": "\033[91m"}
    reset = "\033[0m"
    color = colors.get(rec, "")

    print("\n" + "=" * 60)
    print(f"  Applicant : {application['name']}")
    print(f"  Role      : {application['role']}")
    print(f"  Score     : {score}/10")
    print(f"  Decision  : {color}{rec}{reset}")
    print("-" * 60)
    print(f"  Strengths : {result['strengths']}")
    print(f"  Gaps      : {result['gaps']}")
    print(f"  Summary   : {result['one_line_summary']}")
    print("-" * 60)
    print("  AUTO-REPLY EMAIL:")
    print(f"  {email.replace(chr(10), chr(10) + '  ')}")
    print("=" * 60)


# ── Sample Applications ────────────────────────────────────────────────────────

SAMPLE_APPLICATIONS = [
    {
        "name": "Priya Mehta",
        "email": "priya.mehta@example.com",
        "role": "Social Media & Content Intern",
        "background": "Final year B.A. Mass Communication student at Delhi University.",
        "skills": "Content writing, Canva, Instagram management, basic video editing.",
        "motivation": (
            "I am passionate about education and have volunteered with 2 NGOs previously. "
            "I want to use my communication skills to amplify Vriddhikar's mission "
            "and reach more students across India."
        ),
    },
    {
        "name": "Rohan Singh",
        "email": "rohan.s@example.com",
        "role": "AI Agent Development Intern",
        "background": "1st year B.Com student.",
        "skills": "MS Excel, basic typing.",
        "motivation": "I want to learn new things and gain experience.",
    },
]


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Add it to the .env file in this folder:")
        print("  ANTHROPIC_API_KEY=your_key_here")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("\nVriddhikar Society — AI Application Screening Agent")
    print(f"Processing {len(SAMPLE_APPLICATIONS)} application(s)...\n")

    for application in SAMPLE_APPLICATIONS:
        print(f"Screening: {application['name']} ({application['role']})...")

        screening_result = screen_application(client, application)
        ack_email = generate_acknowledgement(client, application["name"], application["role"])

        print_result(application, screening_result, ack_email)

    print("\nDone. In the full workflow, results would be saved to Google Sheets.")


if __name__ == "__main__":
    main()
