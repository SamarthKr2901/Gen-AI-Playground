"""
PDF Generator for Assignment Submission
Converts Samarth_Kumar_AIAgentIntern.md -> Samarth_Kumar_AIAgentIntern.pdf

Usage:
    pip install fpdf2
    python generate_pdf.py
"""

from fpdf import FPDF
import os

OUTPUT_FILE = "Samarth_Kumar_AIAgentIntern.pdf"


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "AI Workflow & Agent Design  |  Samarth Kumar  |  Vriddhikar Society", align="R")
        self.ln(2)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def add_title_page(pdf: PDF):
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 12, "AI Workflow & Agent Design", align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, "Assignment Submission", align="C")
    pdf.ln(20)

    pdf.set_draw_color(60, 100, 180)
    pdf.set_line_width(0.5)
    pdf.line(50, pdf.get_y(), 160, pdf.get_y())
    pdf.ln(16)

    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(50, 50, 50)
    details = [
        ("Name", "Samarth Kumar"),
        ("Role Applied For", "AI Agent Development Intern"),
        ("Organization", "Vriddhikar Society"),
    ]
    for label, value in details:
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(55, 8, f"{label}:", align="R")
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 8, f"  {value}")
        pdf.ln(7)


def add_section_heading(pdf: PDF, text: str):
    pdf.ln(4)
    pdf.set_fill_color(240, 244, 255)
    pdf.set_text_color(30, 60, 130)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 9, f"  {text}", fill=True)
    pdf.ln(6)
    pdf.set_text_color(30, 30, 30)


def add_body(pdf: PDF, text: str):
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 6, text)
    pdf.ln(2)


def add_code_block(pdf: PDF, text: str):
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(210, 210, 210)
    pdf.set_font("Courier", "", 9)
    pdf.set_text_color(30, 30, 30)
    pdf.set_line_width(0.3)
    lines = text.strip().split("\n")
    block_h = len(lines) * 5 + 6
    pdf.rect(10, pdf.get_y(), 190, block_h, style="FD")
    pdf.set_xy(13, pdf.get_y() + 3)
    for line in lines:
        pdf.cell(0, 5, line)
        pdf.ln(5)
        pdf.set_x(13)
    pdf.ln(4)
    pdf.set_text_color(40, 40, 40)


def add_subheading(pdf: PDF, text: str):
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 7, text)
    pdf.ln(5)


def build_pdf():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(10, 14, 10)
    pdf.set_auto_page_break(auto=True, margin=14)

    add_title_page(pdf)

    # -- Section 1 --------------------------------------------------------------
    pdf.add_page()
    add_section_heading(pdf, "Section 1 - Problem Statement")
    add_body(pdf,
        "So the problem I picked is something that I think most small organizations deal with -- "
        "getting too many applications and not having enough time to go through all of them properly. "
        "For a non-profit like Vriddhikar Society, the team is usually small and people are wearing "
        "multiple hats, so spending hours screening applications every hiring cycle is a real issue.\n\n"
        "Basically, when applications come in through a Google Form or email, someone has to manually "
        "open each one, read through it, figure out if the person is a good fit, and then decide "
        "whether to call them. If there are 30-40 applications, that takes a lot of time and honestly "
        "it's easy to miss good candidates or make inconsistent decisions when you're tired.\n\n"
        "AI can help here because reading text, comparing it against criteria, and giving a score is "
        "exactly the kind of task AI is good at. It doesn't get tired, it applies the same logic to "
        "every application, and it can process 40 in the time it takes a human to read 2. The team "
        "can then just look at the top candidates instead of going through everything themselves."
    )

    # -- Section 2 --------------------------------------------------------------
    add_section_heading(pdf, "Section 2 - AI Workflow Design")
    add_subheading(pdf, "Task: Volunteer / Internship Application Screening")
    steps = [
        ("Step 1 - Input",
         "The applicant fills a Google Form. It asks for basic info like name, email, what role "
         "they're applying for, their background, skills, and a short motivation statement."),
        ("Step 2 - Trigger",
         "As soon as a new form response comes in, Zapier picks it up automatically. This is where "
         "the automation starts -- no human has to do anything at this point."),
        ("Step 3 - AI Processing",
         "Zapier sends the application details to a Python script (or directly to the Claude API). "
         "The AI reads the application, checks relevance for the role, and returns a score out of 10 "
         "along with a short summary of strengths and gaps."),
        ("Step 4 - Store Results",
         "The AI's output gets saved back into a Google Sheet. Each row now has the original "
         "application info plus the AI's score and summary right next to it."),
        ("Step 5 - Notify",
         "Two things happen automatically -- the applicant gets a confirmation email, and the HR "
         "person gets a daily summary email with all new applications and their scores."),
    ]
    for title, desc in steps:
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 6, title)
        pdf.ln(5)
        add_body(pdf, desc)

    # -- Section 3 --------------------------------------------------------------
    pdf.add_page()
    add_section_heading(pdf, "Section 3 - Prompt Engineering")
    add_body(pdf,
        "I used two prompts in this workflow. The first one is for screening the application, and "
        "the second one is for generating the reply email to the applicant. I iterated on the "
        "screening prompt a few times because the first version was giving vague answers -- adding "
        "a clear scoring guide made the output much more consistent."
    )
    add_subheading(pdf, "Prompt 1 - Application Screening")
    add_code_block(pdf,
        "You are an HR screening assistant for Vriddhikar Society, a non-profit that works\n"
        "in education. You screen volunteer and internship applications honestly and briefly.\n"
        "Always reply in valid JSON only.\n\n"
        "Review this application for the role of {role}:\n\n"
        "Name: {name}\n"
        "Background: {background}\n"
        "Skills: {skills}\n"
        "Motivation: {motivation}\n\n"
        'Give your response as a JSON object with these fields:\n'
        '{\n'
        '  "score": a number from 1 to 10,\n'
        '  "strengths": "2-3 sentences on what the candidate does well",\n'
        '  "gaps": "1-2 sentences on what\'s missing or weak",\n'
        '  "recommendation": "Shortlist or Hold or Reject",\n'
        '  "one_line_summary": "one sentence summary for the HR team"\n'
        '}\n\n'
        "Scoring:\n"
        "- 8 to 10: good fit, clear motivation, relevant skills -> Shortlist\n"
        "- 5 to 7:  some fit, worth reviewing -> Hold\n"
        "- 1 to 4:  not a fit, vague motivation -> Reject"
    )
    add_subheading(pdf, "Prompt 2 - Acknowledgement Email")
    add_code_block(pdf,
        "Write a short friendly email to {name} confirming that Vriddhikar Society got their\n"
        "application for the {role} position. Tell them they'll hear back in 5-7 business days.\n"
        "Keep it under 80 words and don't make any promises about selection."
    )

    # -- Section 4 --------------------------------------------------------------
    pdf.add_page()
    add_section_heading(pdf, "Section 4 - Sample Input & Output")
    add_body(pdf, "Here are two examples showing how the AI handles different types of applicants.")

    add_subheading(pdf, "Example 1 -- Good Candidate")
    add_subheading(pdf, "Input:")
    add_code_block(pdf,
        "Name: Priya Mehta\n"
        "Role: Social Media & Content Intern\n"
        "Background: Final year B.A. Mass Communication, Delhi University\n"
        "Skills: Content writing, Canva, Instagram management, basic video editing\n"
        "Motivation: I've volunteered with 2 NGOs before and really care about education access.\n"
        "            I want to use my content skills to help Vriddhikar reach more students."
    )
    add_subheading(pdf, "AI Output:")
    add_code_block(pdf,
        '{\n'
        '  "score": 9,\n'
        '  "strengths": "Priya\'s background in mass communication is directly relevant.\n'
        '               She has NGO experience showing she understands the non-profit space,\n'
        '               and her motivation is specific and genuine.",\n'
        '  "gaps": "Could benefit from experience with social media analytics tools.",\n'
        '  "recommendation": "Shortlist",\n'
        '  "one_line_summary": "Strong content background, real NGO experience -- shortlist."\n'
        '}'
    )
    pdf.ln(2)
    add_subheading(pdf, "Example 2 -- Weak Candidate")
    add_subheading(pdf, "Input:")
    add_code_block(pdf,
        "Name: Rohan Singh\n"
        "Role: AI Agent Development Intern\n"
        "Background: 1st year B.Com student\n"
        "Skills: MS Excel, basic typing\n"
        "Motivation: I want to learn new things and gain some experience."
    )
    add_subheading(pdf, "AI Output:")
    add_code_block(pdf,
        '{\n'
        '  "score": 2,\n'
        '  "strengths": "Open to learning, which is a good attitude.",\n'
        '  "gaps": "No technical skills relevant to AI or programming. Motivation doesn\'t\n'
        '           show understanding of the role or why Vriddhikar specifically.",\n'
        '  "recommendation": "Reject",\n'
        '  "one_line_summary": "No relevant background and generic motivation -- not a fit."\n'
        '}'
    )

    # -- Section 5 --------------------------------------------------------------
    pdf.add_page()
    add_section_heading(pdf, "Section 5 - Tools Used")
    tools = [
        ("Claude AI (Anthropic)", "The AI model doing the actual screening and writing the emails"),
        ("Python + anthropic SDK", "The script that connects everything and calls the API"),
        ("Google Forms", "Where applicants submit their info"),
        ("Google Sheets", "Stores all applications plus AI results in one place"),
        ("Zapier", "Handles automation between Forms, the AI script, and Gmail"),
        ("Gmail", "Sends the auto-reply confirmation emails to applicants"),
        ("Claude Code", "Used to write and test the Python script and prompts"),
    ]
    for tool, purpose in tools:
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(55, 6, tool)
        pdf.set_font("Helvetica", "", 10.5)
        pdf.set_text_color(70, 70, 70)
        pdf.cell(0, 6, f"-- {purpose}")
        pdf.ln(7)

    # -- Section 6 --------------------------------------------------------------
    add_section_heading(pdf, "Section 6 - Automation Logic")
    add_body(pdf,
        "The whole point of this workflow is that after setup, you don't have to touch it. "
        "Here's what happens without any human involvement:"
    )
    auto_steps = [
        "Someone submits the Google Form",
        "Zapier detects the new response immediately",
        "Zapier sends the data to the Claude API",
        "Claude returns the score and summary as JSON",
        "Zapier writes that back into the Google Sheet as new columns",
        "Zapier sends a confirmation email to the applicant through Gmail",
        "Every morning at 9 AM, a scheduled Zapier task sends the HR team a digest email "
        "with all applications from the last 24 hours that scored 5 or above",
    ]
    for i, step in enumerate(auto_steps, 1):
        pdf.set_font("Helvetica", "", 10.5)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(8, 6, f"{i}.")
        pdf.multi_cell(0, 6, step)
        pdf.ln(1)

    pdf.ln(4)
    add_body(pdf,
        "The only time a human gets involved is when they open that digest email, look at the "
        "shortlisted names, and decide who to call for an interview. Everything before that point "
        "runs automatically.\n\n"
        "This means instead of reading through 30+ applications, the HR team is looking at maybe "
        "5-8 that the AI has already flagged as worth their time."
    )

    # -- Footer -----------------------------------------------------------------
    pdf.ln(10)
    pdf.set_draw_color(180, 180, 180)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 6, "Submitted by Samarth Kumar  |  AI Agent Development Intern Application  |  Vriddhikar Society", align="C")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, OUTPUT_FILE)
    pdf.output(out_path)
    print(f"PDF saved: {out_path}")


if __name__ == "__main__":
    build_pdf()
