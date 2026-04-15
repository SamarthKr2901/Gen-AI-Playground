# Samarth_Kumar_AIAgentIntern

AI Workflow & Agent Design assignment submission for Vriddhikar Society.

## Task Automated
**Volunteer / Internship Application Screening** using Claude AI.

## Files

| File | Description |
|------|-------------|
| `Samarth_Kumar_AIAgentIntern.md` | Main submission document (all 6 sections) |
| `agent.py` | Python demo script — calls Claude API to screen applications |
| `sample_data/sample_application_1.txt` | Sample input + expected output (strong candidate) |
| `sample_data/sample_application_2.txt` | Sample input + expected output (weak candidate) |

## Running the Demo

1. Install dependencies:
   ```
   pip install anthropic python-dotenv
   ```

2. Add your API key to the `.env` file (copy from `.env.example`):
   ```
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```

3. Run:
   ```
   python agent.py
   ```

## Getting an Anthropic API Key
- Visit: https://console.anthropic.com
- Sign up / log in → API Keys → Create Key
- Free tier credits are available for new accounts

## Workflow Summary

```
Google Form → Zapier Trigger → Claude API → Google Sheets → Email Notification
```
