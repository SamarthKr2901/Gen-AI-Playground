**Name:** Samarth Kumar
**Role Applied For:** AI Agent Development Intern
**Organization:** Vriddhikar Society

---

## Section 1 – Problem Statement

So the problem I picked is something that I think most small organizations deal with — getting too many applications and not having enough time to go through all of them properly. For a non-profit like Vriddhikar Society, the team is usually small and people are wearing multiple hats, so spending hours screening applications every hiring cycle is a real issue.

Basically, when applications come in through a Google Form or email, someone has to manually open each one, read through it, figure out if the person is a good fit, and then decide whether to call them. If there are 30-40 applications, that takes a lot of time and honestly it's easy to miss good candidates or make inconsistent decisions when you're tired.

AI can help here because reading text, comparing it against criteria, and giving a score is exactly the kind of task AI is good at. It doesn't get tired, it applies the same logic to every application, and it can do 40 in the time it takes a human to read 2. The team can then just look at the top candidates instead of going through everything themselves.

---

## Section 2 – AI Workflow Design

**Task:** Volunteer / Internship Application Screening

Here's how the whole thing works step by step:

**Step 1 – Input**
The applicant fills a Google Form. It asks for basic info like name, email, what role they're applying for, their background, skills, and a short motivation statement. Pretty standard stuff.

**Step 2 – Trigger**
As soon as a new form response comes in, Zapier picks it up automatically. This is the part where the automation actually starts — no human has to do anything at this point.

**Step 3 – AI Processing**
Zapier sends the application details to a Python script (or directly to the Claude API via webhook). The AI reads the application, checks how relevant the person is for the role, and gives back a score out of 10 along with a short summary of their strengths and what's missing.

**Step 4 – Store Results**
The AI's output gets saved back into a Google Sheet. So now each row in the sheet has the original application info plus the AI's score and summary right next to it. Makes it really easy to sort and review.

**Step 5 – Notify**
Two things happen automatically — the applicant gets a confirmation email saying their application was received, and the HR person gets a daily summary email with all the new applications and their scores so they can quickly see who to focus on.

---

## Section 3 – Prompt Engineering

I used two prompts in this workflow. The first one is for screening the application, and the second one is for generating the reply email to the applicant.

I iterated on the screening prompt a few times because the first version was giving vague answers. Adding a scoring guide with clear ranges made the output much more consistent.

**Prompt 1 – Application Screening**

```
You are an HR screening assistant for Vriddhikar Society, a non-profit that works
in education. You screen volunteer and internship applications honestly and briefly.
Always reply in valid JSON only.

Review this application for the role of {role}:

Name: {name}
Background: {background}
Skills: {skills}
Motivation: {motivation}

Give your response as a JSON object with these fields:
{
  "score": a number from 1 to 10,
  "strengths": "2-3 sentences on what the candidate does well",
  "gaps": "1-2 sentences on what's missing or weak",
  "recommendation": "Shortlist or Hold or Reject",
  "one_line_summary": "one sentence summary for the HR team"
}

Scoring:
- 8 to 10: good fit, clear motivation, relevant skills → Shortlist
- 5 to 7: some fit, worth reviewing → Hold
- 1 to 4: not a fit, vague motivation → Reject
```

**Prompt 2 – Acknowledgement Email**

```
Write a short friendly email to {name} confirming that Vriddhikar Society got their
application for the {role} position. Tell them they'll hear back in 5-7 business days.
Keep it under 80 words and don't make any promises about whether they'll be selected.
```

---

## Section 4 – Sample Input & Output

Here are two examples showing how the AI handles different types of applicants.

---

**Example 1 — Good Candidate**

Input:
```
Name: Priya Mehta
Role: Social Media & Content Intern
Background: Final year B.A. Mass Communication, Delhi University
Skills: Content writing, Canva, Instagram management, basic video editing
Motivation: I've volunteered with 2 NGOs before and really care about education access.
I want to use my content skills to help Vriddhikar reach more students.
```

AI Output:
```json
{
  "score": 9,
  "strengths": "Priya's background in mass communication is directly relevant to the role. She already has hands-on NGO experience which shows she understands the non-profit space, and her motivation is specific and genuine.",
  "gaps": "Could benefit from some experience with social media analytics tools but this is minor.",
  "recommendation": "Shortlist",
  "one_line_summary": "Strong content background, real NGO experience, clearly aligned with the mission — shortlist."
}
```

Auto-reply email sent to Priya:
```
Subject: Got your application – Vriddhikar Society

Hi Priya,

Thanks for applying for the Social Media & Content Intern role at Vriddhikar Society!
We've received your application and will go through it soon.

Expect to hear back from us in 5–7 business days.

Thanks,
Team Vriddhikar
```

---

**Example 2 — Weak Candidate**

Input:
```
Name: Rohan Singh
Role: AI Agent Development Intern
Background: 1st year B.Com student
Skills: MS Excel, basic typing
Motivation: I want to learn new things and gain some experience.
```

AI Output:
```json
{
  "score": 2,
  "strengths": "Open to learning, which is a good attitude.",
  "gaps": "No technical skills relevant to AI or programming. The motivation doesn't show any understanding of what the role involves or why Vriddhikar specifically.",
  "recommendation": "Reject",
  "one_line_summary": "No relevant technical background and very generic motivation — not a fit for this role."
}
```

---

## Section 5 – Tools Used

- **Claude AI (Anthropic)** — the AI model doing the actual screening and writing the emails
- **Python** with the `anthropic` library — the script that connects everything
- **Google Forms** — where applicants submit their info
- **Google Sheets** — stores all applications plus AI results in one place
- **Zapier** — handles the automation between Forms, the AI script, and Gmail
- **Gmail** — sends the auto-reply to applicants
- **Claude Code** — used to write and test the Python script and prompts

---

## Section 6 – Automation Logic (How it runs on its own)

The whole point of this workflow is that after setup, you don't have to touch it.

Here's what happens without any human involvement:

1. Someone submits the Google Form
2. Zapier detects the new response immediately
3. Zapier sends the data to the Claude API
4. Claude returns the score and summary as JSON
5. Zapier writes that back into the Google Sheet as new columns
6. Zapier sends a confirmation email to the applicant through Gmail
7. Every morning at 9 AM, a scheduled Zapier task sends the HR team a digest email with all applications from the last 24 hours that scored 5 or above

The only time a human gets involved is when they open that digest email, look at the shortlisted names, and decide who to call for an interview. Everything before that point runs automatically.

This means instead of reading through 30+ applications, the HR team is looking at maybe 5-8 that the AI has already flagged as worth their time.

---

*Submitted by Samarth Kumar*
