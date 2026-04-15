from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT = r"C:\Users\evils\Desktop\Work\ApexWindows\WF2_API_Reference.pdf"

PURPLE_BG   = (74, 20, 140)
PURPLE_LITE = (206, 147, 216)
PURPLE_PALE = (237, 231, 246)
GREEN_BTN   = (46, 125, 50)
GREY_HDR    = (245, 245, 245)
GREY_LINE   = (200, 200, 200)
ORANGE      = (230, 81, 0)
BLUE        = (13, 71, 161)
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*[150]*3)
        self.cell(0, 6, "ApexWindows TX  -  WF2 API Reference  |  Postman Test Collection", align="L")
        self.set_y(self.get_y() - 6)
        self.cell(0, 6, f"Page {self.page_no()}", align="R")
        self.ln(2)
        self.set_draw_color(*GREY_LINE)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
        self.set_text_color(*BLACK)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*[150]*3)
        self.cell(0, 8, "Confidential  -  ApexWindows TX Internal Documentation  -  Generated 2026-04-13", align="C")

    # ------------------------------------------------------------------ helpers
    def cover(self):
        self.add_page()
        self.set_fill_color(*PURPLE_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_y(55)
        self.set_font("Helvetica", "B", 32)
        self.set_text_color(*WHITE)
        self.cell(0, 14, "ApexWindows TX", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*PURPLE_LITE)
        self.cell(0, 10, "Automation System  -  WF2", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)
        self.set_font("Helvetica", "", 13)
        self.set_text_color(220, 200, 255)
        self.cell(0, 8, "Quote Approval & Payment Pipeline", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)
        self.set_draw_color(*PURPLE_LITE)
        self.line(35, self.get_y(), 175, self.get_y())
        self.ln(10)
        self.set_font("Helvetica", "B", 15)
        self.set_text_color(*WHITE)
        self.cell(0, 9, "WF2 Webhook API Reference", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(220, 200, 255)
        self.cell(0, 8, "Postman Collection  -  Flows A through E", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(28)
        # info box
        bx, by = 30, self.get_y()
        self.set_fill_color(255, 255, 255, )
        self.set_draw_color(*PURPLE_LITE)
        self.set_fill_color(40, 10, 80)
        self.rect(bx, by, 150, 62, "FD")
        self.set_xy(bx + 6, by + 6)
        rows = [
            ("Base URL",       "https://vmi3106842.contaboserver.net"),
            ("n8n Workflow",   "u3bAOVE5cXwraYaZ  (WF2 - LIVE)"),
            ("Supabase",       "ioulhoifgcznyezofywb.supabase.co"),
            ("Test Lead ID",   "6b1761d9-9766-4455-99f4-5a47b0312247"),
            ("Test Invoice",   "APX-2026-TEST1"),
            ("Postman WS",     "Samarth Kumar's Workspace"),
        ]
        for label, val in rows:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(*PURPLE_LITE)
            self.cell(38, 8, label + ":", new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*WHITE)
            self.cell(0, 8, val, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_x(bx + 6)
        self.ln(20)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(*PURPLE_LITE)
        self.cell(0, 8, "Generated: 2026-04-13  -  OyeLabs", align="C")

    def section_title(self, title, subtitle=""):
        self.ln(4)
        self.set_fill_color(*PURPLE_BG)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 10, "  " + title, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if subtitle:
            self.set_fill_color(*PURPLE_PALE)
            self.set_text_color(74, 20, 140)
            self.set_font("Helvetica", "I", 9)
            self.cell(0, 7, "  " + subtitle, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)
        self.ln(3)

    def kv(self, key, val, key_w=42):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(74, 20, 140)
        self.cell(key_w, 6, key, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*BLACK)
        self.cell(0, 6, val, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def method_badge(self, method, url):
        """Print a method badge + URL on one line."""
        colors = {"POST": GREEN_BTN, "GET": BLUE, "PATCH": ORANGE}
        bg = colors.get(method, BLACK)
        self.set_fill_color(*bg)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 9)
        self.cell(14, 7, method, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(30, 30, 30)
        self.set_font("Courier", "", 9)
        self.cell(0, 7, "  " + url, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)

    def code_block(self, lines):
        self.set_fill_color(30, 30, 30)
        self.set_text_color(200, 255, 200)
        self.set_font("Courier", "", 8)
        padding = 4
        self.set_x(self.l_margin)
        for line in lines:
            self.cell(0, 5.5, "  " + line, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # close bottom
        self.set_fill_color(30, 30, 30)
        self.cell(0, padding - 1, "", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)
        self.ln(2)

    def prereq_box(self, items):
        self.set_fill_color(255, 248, 225)
        self.set_draw_color(255, 193, 7)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(121, 85, 7)
        self.cell(0, 7, "  !  PRE-TEST REQUIREMENTS", fill=True, border="LTR",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "", 8.5)
        for item in items:
            self.set_fill_color(255, 253, 240)
            self.set_x(self.l_margin)
            self.cell(5, 6, "", fill=True, border="L", new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_text_color(60, 40, 0)
            self.multi_cell(0, 6, "  " + item, fill=True, border="R")
        self.set_fill_color(255, 248, 225)
        self.cell(0, 3, "", fill=True, border="LBR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)
        self.ln(2)

    def outcome_box(self, items):
        self.set_fill_color(232, 245, 233)
        self.set_draw_color(76, 175, 80)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(27, 94, 32)
        self.cell(0, 7, "  OK  EXPECTED OUTCOMES", fill=True, border="LTR",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "", 8.5)
        for item in items:
            self.set_fill_color(245, 255, 245)
            self.set_x(self.l_margin)
            self.cell(5, 6, "", fill=True, border="L", new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_text_color(20, 60, 20)
            self.multi_cell(0, 6, "  " + item, fill=True, border="R")
        self.set_fill_color(232, 245, 233)
        self.cell(0, 3, "", fill=True, border="LBR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)
        self.ln(3)

    def h3(self, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(74, 20, 140)
        self.cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*BLACK)

    def divider(self):
        self.ln(2)
        self.set_draw_color(*GREY_LINE)
        self.line(self.l_margin, self.get_y(), 200, self.get_y())
        self.ln(4)


# ======================================================================== FLOWS
def add_toc(pdf):
    pdf.add_page()
    pdf.section_title("Table of Contents")
    entries = [
        ("1", "Quick-Start Checklist & Test Variables", "3"),
        ("2", "Flow A  -  Quote Approval Ready", "4"),
        ("3", "Flow B  -  Manager Approved", "5"),
        ("4", "Flow C  -  Customer Accepted Quote", "6"),
        ("5", "Flow D  -  Job Completed", "7"),
        ("6", "Flow E (Manual)  -  Payment Received", "8"),
        ("7", "Flow E (Stripe)  -  Stripe Payment Webhook", "9"),
        ("8", "DB Reset SQL Reference", "10"),
    ]
    pdf.set_font("Helvetica", "", 10)
    for num, title, pg in entries:
        pdf.set_text_color(74, 20, 140)
        pdf.cell(8, 8, num + ".", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_text_color(*BLACK)
        pdf.cell(160, 8, title, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 8, pg, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_draw_color(*GREY_LINE)
        pdf.line(pdf.l_margin, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 8.5)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6,
        "Note: All calls require the WF2 webhook to be in Execute mode in n8n before firing. "
        "The n8n server is at https://vmi3106842.contaboserver.net. Webhooks respond immediately "
        "(responseMode: onReceived) - you will get HTTP 200 before the workflow completes.")


def add_variables_page(pdf):
    pdf.add_page()
    pdf.section_title("1. Quick-Start Checklist & Test Variables",
                       "Set these Postman collection variables before running any flow")

    pdf.h3("Collection Variables")
    rows = [
        ("base_url",          "https://vmi3106842.contaboserver.net",          "n8n server - do not change"),
        ("lead_id",           "6b1761d9-9766-4455-99f4-5a47b0312247",          "Test lead UUID - reset pipeline_stage before use"),
        ("estimate_id",       "REPLACE_WITH_ESTIMATE_ID",                       "UUID from estimates table for test lead"),
        ("acceptance_token",  "testtoken_flowE_demo",                           "Must match acceptance_token in quotes table"),
        ("invoice_number",    "APX-2026-TEST1",                                 "Must match invoice in invoices table - reset to unpaid"),
    ]
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(38, 7, "Variable", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(78, 7, "Default Value", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Notes", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 7.5)
    pdf.set_text_color(*BLACK)
    for var, val, note in rows:
        pdf.cell(38, 6, var, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Courier", "", 7)
        pdf.cell(78, 6, val, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 7.5)
        pdf.cell(0,  6, note, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Courier", "", 7.5)

    pdf.ln(5)
    pdf.h3("Full Pipeline Reset (run before a full A->E demo)")
    sql = [
        "-- 1. Reset lead pipeline stage",
        "UPDATE leads SET pipeline_stage = 'Estimate Generated'",
        "  WHERE id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
        "",
        "-- 2. Reset / create quote",
        "UPDATE quotes SET status = 'pending_approval', accepted_at = NULL",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
        "",
        "-- 3. Reset invoice",
        "UPDATE invoices SET status = 'unpaid', amount_paid = 0, paid_at = NULL",
        "  WHERE invoice_number = 'APX-2026-TEST1';",
        "",
        "-- 4. Reopen escalations",
        "UPDATE escalations SET resolved = FALSE, resolved_at = NULL",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
    ]
    pdf.code_block(sql)

    pdf.h3("Flow-by-Flow Execution Order")
    steps = [
        ("Flow A", "POST /webhook/quote-approval-ready",  "Fires after WF1 generates estimate. Creates quote record."),
        ("Flow B", "POST /webhook/manager-approved",      "SM approves quote. Sends customer quote email."),
        ("Flow C", "GET  /webhook/customer-accepted",     "Customer clicks accept link. Invoice created."),
        ("Flow D", "POST /webhook/job-completed",         "Job done on-site. Invoice emailed to customer."),
        ("Flow E", "POST /webhook/payment-received  OR",  "Payment confirmed. Lead Closed Won. WF3 triggered."),
        ("",       "POST /webhook/stripe-payment",        "(Stripe auto-fires this in production)"),
    ]
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(18, 7, "Flow", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(72, 7, "Endpoint", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Purpose", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(*BLACK)
    for fl, ep, purpose in steps:
        pdf.set_font("Helvetica", "B", 8)
        pdf.cell(18, 6, fl, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Courier", "", 7.5)
        pdf.cell(72, 6, ep, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 8)
        pdf.cell(0,  6, purpose, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def add_flow_a(pdf):
    pdf.add_page()
    pdf.section_title("2. Flow A  -  Quote Approval Ready",
                       "Triggered by WF1 after AI estimate is generated. Creates quote record and notifies Sales Manager.")
    pdf.kv("Endpoint", "POST {{base_url}}/webhook/quote-approval-ready")
    pdf.kv("Triggered by", "WF1 (automated) - also callable manually for testing")
    pdf.kv("Auth", "None required")
    pdf.ln(3)

    pdf.h3("Request Headers")
    pdf.method_badge("POST", "/webhook/quote-approval-ready")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(55, 7, "Header", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Value", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 8)
    pdf.set_text_color(*BLACK)
    pdf.cell(55, 6, "Content-Type", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  6, "application/json", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Request Body (JSON)")
    pdf.code_block([
        "{",
        '  "lead_id":     "{{lead_id}}",          // UUID - must exist in leads table',
        '  "estimate_id": "{{estimate_id}}"        // UUID - must exist in estimates table',
        "}",
    ])

    pdf.prereq_box([
        "Lead record exists in `leads` table with pipeline_stage = 'Estimate Generated' (or earlier)",
        "Estimate record exists in `estimates` table - get the UUID from: SELECT id FROM estimates WHERE lead_id = '{{lead_id}}'",
        "Update the {{estimate_id}} Postman variable with the real UUID before sending",
        "WF2 webhook must be active and listening (n8n Execute mode or workflow is Active)",
    ])

    pdf.outcome_box([
        "Quote record created in `quotes` table with status = 'pending_approval' and acceptance_token set",
        "pipeline_stage updated to 'Quote Pending Approval'",
        "Email sent to alvin@apexwindowstx.com with estimate summary and CRM approval link",
        "activity_log entry: event_type = 'quote_approval_queued'",
        "Response: HTTP 200 (immediate - responseMode: onReceived)",
    ])

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "workflow_triggered"}',
        "",
        "// Note: onReceived mode - workflow continues async after this 200",
        "// Check Supabase to verify pipeline_stage updated",
    ])

    pdf.divider()
    pdf.h3("Notes")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.multi_cell(0, 6,
        "In production this call is made automatically by WF1 after the AI estimate is generated. "
        "For manual testing, you must first have a valid lead + estimate in the DB. "
        "The acceptance_token generated here is the customer's unique link - it's a 64-char hex string "
        "that grants access to the accept/decline page.")


def add_flow_b(pdf):
    pdf.add_page()
    pdf.section_title("3. Flow B  -  Manager Approved",
                       "Sales Manager approves the quote. Triggers branded quote email to customer.")
    pdf.kv("Endpoint", "POST {{base_url}}/webhook/manager-approved")
    pdf.kv("Triggered by", "CRM 'Approve & Send' button (manual - human gate)")
    pdf.kv("Auth", "None required")
    pdf.ln(3)

    pdf.h3("Request Headers")
    pdf.method_badge("POST", "/webhook/manager-approved")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(55, 7, "Header", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Value", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 8)
    pdf.set_text_color(*BLACK)
    pdf.cell(55, 6, "Content-Type", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  6, "application/json", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Request Body (JSON)")
    pdf.code_block([
        "{",
        '  "lead_id":         "{{lead_id}}",   // UUID - must match quote in DB',
        '  "approved_by":     "Alvin",          // "Alvin" or "Dan"',
        '  "adjusted_amount": null              // optional - omit or null to use original estimate',
        "}",
        "",
        "// Example with price override:",
        "{",
        '  "lead_id":         "{{lead_id}}",',
        '  "approved_by":     "Dan",',
        '  "adjusted_amount": 920.00',
        "}",
    ])

    pdf.prereq_box([
        "Flow A must have run first - quotes table must have a row with status = 'pending_approval' for this lead",
        "pipeline_stage = 'Quote Pending Approval' in leads table",
        "If testing standalone: INSERT a quote row manually with status = 'pending_approval' and an acceptance_token",
    ])

    pdf.outcome_box([
        "Quote status updated to 'sent', approved_by + approved_at + sent_at timestamps set",
        "If adjusted_amount provided: estimates table updated with adjusted_total, manually_adjusted = true",
        "pipeline_stage updated to 'Quote Sent'",
        "Branded quote email sent to customer with Accept / Decline buttons",
        "72-hour escalation created in escalations table (type = customer_not_responded)",
        "Email sent to Sales Manager confirming quote was sent",
        "activity_log entry: event_type = 'quote_sent'",
    ])

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "workflow_triggered"}',
    ])

    pdf.divider()
    pdf.h3("Notes")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.multi_cell(0, 6,
        "This is the human-in-the-loop gate - no quote ever reaches the customer without this step. "
        "The customer email currently goes to samarth.kumar2901@gmail.com (test). "
        "Before go-live, update the toEmail node to use the actual lead_email from the DB. "
        "The accept/decline buttons link to apexwindowstx.com/quote/accept?token=... (frontend not yet built).")


def add_flow_c(pdf):
    pdf.add_page()
    pdf.section_title("4. Flow C  -  Customer Accepted Quote",
                       "Customer clicks the Accept button in their quote email. GET request with token param.")
    pdf.kv("Endpoint", "GET {{base_url}}/webhook/customer-accepted?token={{acceptance_token}}")
    pdf.kv("Triggered by", "Customer clicking Accept link in quote email (frontend page POSTs token)")
    pdf.kv("Auth", "Token in query string acts as auth")
    pdf.ln(3)

    pdf.h3("Request")
    pdf.method_badge("GET", "/webhook/customer-accepted?token={{acceptance_token}}")
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(100, 60, 0)
    pdf.multi_cell(0, 6,
        "No request body required. The acceptance_token query parameter is the sole identifier. "
        "It must exactly match the acceptance_token stored in the quotes table for this lead.")
    pdf.set_text_color(*BLACK)
    pdf.ln(3)

    pdf.h3("Query Parameters")
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(38, 7, "Parameter", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(55, 7, "Value", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Notes", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 8)
    pdf.set_text_color(*BLACK)
    pdf.cell(38, 6, "token", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(55, 6, "{{acceptance_token}}", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 8)
    pdf.cell(0,  6, "64-char hex - must match quotes.acceptance_token in DB", border=1,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("How to get the real token for testing")
    pdf.code_block([
        "-- Get the actual acceptance_token for your test lead:",
        "SELECT acceptance_token FROM quotes",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247'",
        "  AND status = 'sent'",
        "  LIMIT 1;",
        "",
        "-- Then update the Postman {{acceptance_token}} variable with this value",
    ])

    pdf.prereq_box([
        "Flow B must have run - quotes table must have a row with status = 'sent' for this lead",
        "pipeline_stage = 'Quote Sent'",
        "Update {{acceptance_token}} variable with real value from DB (query above)",
        "Token is case-sensitive and must be an exact match",
    ])

    pdf.outcome_box([
        "Quote status updated to 'accepted', accepted_at timestamp set",
        "pipeline_stage updated to 'Quote Accepted'",
        "Invoice created in invoices table (status = 'unpaid', amount_due = quote total)",
        "72hr customer_not_responded escalation resolved",
        "Confirmation email sent to customer",
        "Email sent to Sales Manager: Quote Accepted - SCHEDULE NOW",
        "activity_log entry: event_type = 'quote_accepted'",
    ])

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "accepted"}',
    ])


def add_flow_d(pdf):
    pdf.add_page()
    pdf.section_title("5. Flow D  -  Job Completed",
                       "Marks physical job as complete. Creates invoice and sends payment link to customer.")
    pdf.kv("Endpoint", "POST {{base_url}}/webhook/job-completed")
    pdf.kv("Triggered by", "CRM 'Mark Completed' button (manual - technician/SM confirms on-site job done)")
    pdf.kv("Auth", "None required")
    pdf.ln(3)

    pdf.h3("Request Headers")
    pdf.method_badge("POST", "/webhook/job-completed")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(55, 7, "Header", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Value", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 8)
    pdf.set_text_color(*BLACK)
    pdf.cell(55, 6, "Content-Type", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  6, "application/json", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Request Body (JSON)")
    pdf.code_block([
        "{",
        '  "lead_id": "{{lead_id}}"   // UUID - required',
        "}",
        "",
        "// Note: marked_by and job_notes are optional fields defined in the WF spec",
        "// but the current live node only reads lead_id from the webhook body",
    ])

    pdf.prereq_box([
        "Flow C must have run - pipeline_stage must be 'Quote Accepted' or 'Scheduled'",
        "An accepted quote must exist (status = 'accepted') to look up amount_due for invoice",
        "Guard rail: if pipeline_stage is already 'Completed', 'Payment Pending', or 'Closed Won' - flow returns already_completed and stops",
    ])

    pdf.outcome_box([
        "pipeline_stage updated to 'Completed', then immediately to 'Payment Pending'",
        "Invoice generated: invoice_number format APX-{YEAR}-{1000-9999}, due_date = today + 14 days",
        "Invoice created in invoices table (status = 'unpaid', amount_due from accepted quote)",
        "leads.invoice_number and invoice_sent_at updated",
        "Stripe Price + Payment Link created for the invoice amount",
        "HTML invoice email sent to customer with 'Pay Now - Secure Stripe Checkout' button",
        "Note: invoice_number is RANDOM - check DB after this call to get real value for Flow E",
    ])

    pdf.h3("Get Invoice Number After Flow D")
    pdf.code_block([
        "-- After running Flow D, get the actual invoice_number for Flow E:",
        "SELECT invoice_number, amount_due, status",
        "FROM invoices",
        "WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247'",
        "ORDER BY created_at DESC LIMIT 1;",
        "",
        "-- Update {{invoice_number}} Postman variable with this value before Flow E",
    ])

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "workflow_triggered"}',
    ])


def add_flow_e_manual(pdf):
    pdf.add_page()
    pdf.section_title("6. Flow E (Manual)  -  Payment Received",
                       "Manual payment entry. Use when payment comes in via cash, check, or bank transfer.")
    pdf.kv("Endpoint", "POST {{base_url}}/webhook/payment-received")
    pdf.kv("Triggered by", "Manual entry - payment confirmed outside Stripe")
    pdf.kv("Auth", "None required")
    pdf.ln(3)

    pdf.h3("Request Headers")
    pdf.method_badge("POST", "/webhook/payment-received")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(55, 7, "Header", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Value", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Courier", "", 8)
    pdf.set_text_color(*BLACK)
    pdf.cell(55, 6, "Content-Type", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  6, "application/json", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Request Body (JSON)")
    pdf.code_block([
        "{",
        '  "invoice_number":  "{{invoice_number}}",   // e.g. "APX-2026-TEST1"',
        '  "amount_paid":     875.00,                  // must be >= amount_due - $0.50 for full payment',
        '  "payment_method":  "cash",                  // cash | check | bank_transfer | other',
        '  "transaction_id":  "MANUAL-TEST-001"        // optional reference number',
        "}",
    ])

    pdf.prereq_box([
        "Flow D must have run - invoice must exist in invoices table with status = 'unpaid'",
        "pipeline_stage = 'Payment Pending'",
        "{{invoice_number}} must match the actual invoice in DB (check after Flow D - number is random)",
        "amount_paid must be >= amount_due - $0.50 to trigger the full payment (Closed Won) path",
        "If amount_paid < amount_due - $0.50: partial payment path fires instead (no Closed Won)",
    ])

    pdf.outcome_box([
        "Invoice status updated to 'paid', amount_paid set, paid_at timestamp set, payment_method stored",
        "pipeline_stage updated to 'Closed Won', closed_won_at timestamp set",
        "ALL open escalations for this lead resolved",
        "Email sent to customer: Payment Received - Thank You",
        "Email sent to Sales Manager: CLOSED WON + amount",
        "WF3 triggered via POST /wf3/closed-won (placeholder URL - continueOnFail: true until WF3 built)",
        "activity_log entry: event_type = 'closed_won'",
    ])

    pdf.h3("Payment Method Options")
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(35, 7, "payment_method", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "When to use", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    methods = [
        ("cash",          "Physical cash payment on-site"),
        ("check",         "Paper check from customer"),
        ("bank_transfer", "ACH / wire transfer"),
        ("other",         "Any other payment type not listed"),
    ]
    pdf.set_text_color(*BLACK)
    for m, desc in methods:
        pdf.set_font("Courier", "", 8)
        pdf.cell(35, 6, m, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 8)
        pdf.cell(0,  6, desc, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "workflow_triggered"}',
        "",
        "// Verify in Supabase:",
        "SELECT pipeline_stage, closed_won_at FROM leads WHERE id = '{{lead_id}}';",
        "SELECT status, amount_paid, paid_at FROM invoices WHERE invoice_number = '{{invoice_number}}';",
    ])


def add_flow_e_stripe(pdf):
    pdf.add_page()
    pdf.section_title("7. Flow E (Stripe)  -  Stripe Payment Webhook",
                       "Simulates Stripe checkout.session.completed event. Production: Stripe fires this automatically.")
    pdf.kv("Endpoint", "POST {{base_url}}/webhook/stripe-payment")
    pdf.kv("Triggered by", "Stripe automatically (production) - manual simulation for testing")
    pdf.kv("Auth", "Stripe-Signature header (ignored in test mode)")
    pdf.ln(3)

    pdf.h3("Request Headers")
    pdf.method_badge("POST", "/webhook/stripe-payment")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(*GREY_HDR)
    pdf.set_text_color(74, 20, 140)
    pdf.cell(55, 7, "Header", fill=True, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(0,  7, "Value", fill=True, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    hdrs = [
        ("Content-Type",    "application/json"),
        ("Stripe-Signature", "t=TEST,v1=TEST_SIGNATURE   (test only - check Stripe config)"),
    ]
    pdf.set_text_color(*BLACK)
    for h, v in hdrs:
        pdf.set_font("Courier", "", 8)
        pdf.cell(55, 6, h, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 8)
        pdf.cell(0,  6, v, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.h3("Request Body (JSON)  -  Stripe checkout.session.completed format")
    pdf.code_block([
        "{",
        '  "type": "checkout.session.completed",',
        '  "data": {',
        '    "object": {',
        '      "id":             "cs_test_postman_001",',
        '      "payment_status": "paid",',
        '      "amount_total":   87500,          // in CENTS - 87500 = $875.00',
        '      "currency":       "usd",',
        '      "payment_intent": "pi_test_postman_001",',
        '      "metadata": {',
        '        "invoice_number": "{{invoice_number}}",  // MUST match DB',
        '        "lead_id":        "{{lead_id}}"',
        '      }',
        '    }',
        '  }',
        "}",
    ])

    pdf.prereq_box([
        "Same as Flow E Manual: invoice must be 'unpaid', pipeline_stage = 'Payment Pending'",
        "metadata.invoice_number must match actual invoice in invoices table",
        "amount_total is in cents - 87500 = $875.00. Node divides by 100 to get dollar amount",
        "Only checkout.session.completed events with payment_status = 'paid' are processed - other events silently return empty array",
        "Stripe webhook must be registered at: Stripe Dashboard -> Developers -> Webhooks -> Add endpoint",
    ])

    pdf.outcome_box([
        "Same outcomes as Flow E Manual path:",
        "Invoice status = 'paid', amount_paid set, paid_at set, payment_method = 'stripe'",
        "transaction_id set to Stripe payment_intent ID (pi_...)",
        "pipeline_stage = 'Closed Won'",
        "All escalations resolved, customer + SM emails sent, WF3 triggered",
        "activity_log: event_type = 'closed_won'",
    ])

    pdf.h3("How the Stripe Path Works in WF2")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.multi_cell(0, 6,
        "The Stripe webhook fires at /webhook/stripe-payment. A 'Parse Stripe Event' code node "
        "filters for checkout.session.completed + paid, extracts invoice_number and amount from metadata. "
        "Both paths (manual and Stripe) merge at 'Normalize Payment', then flow through the same "
        "Validate Invoice -> Payment Check Data -> IF Full Payment -> ... chain.")
    pdf.ln(3)

    pdf.h3("Stripe Account Reference")
    pdf.code_block([
        "Account:         acct_1TLT0hJosmfUu62I  (test mode)",
        "Product:         prod_UK7fOLtQKN18WN  (Window Replacement Service)",
        "Webhook ID:      we_1TLTg7JosmfUu62IWXJiJoMX",
        "Signing secret:  whsec_FuMesdqcIsnWyBQwdo6wf3mpbnr2qzrL",
        "n8n webhook URL: https://vmi3106842.contaboserver.net/webhook/stripe-payment",
    ])

    pdf.h3("Expected Response")
    pdf.code_block([
        "HTTP 200 OK",
        '{"status": "workflow_triggered"}',
    ])


def add_db_reference(pdf):
    pdf.add_page()
    pdf.section_title("8. DB Reset SQL Reference",
                       "Supabase SQL to reset test data between runs. Run in Supabase SQL Editor.")

    pdf.h3("Full Pipeline Reset  (before a complete A->E demo)")
    pdf.code_block([
        "-- Reset lead to post-estimate state",
        "UPDATE leads",
        "  SET pipeline_stage = 'Estimate Generated',",
        "      closed_won_at  = NULL,",
        "      invoice_number = NULL,",
        "      invoice_sent_at = NULL",
        "  WHERE id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
        "",
        "-- Reset quote to pending approval",
        "UPDATE quotes",
        "  SET status        = 'pending_approval',",
        "      accepted_at   = NULL,",
        "      sent_at       = NULL,",
        "      approved_at   = NULL",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
        "",
        "-- Reset invoice",
        "UPDATE invoices",
        "  SET status     = 'unpaid',",
        "      amount_paid = 0,",
        "      paid_at     = NULL,",
        "      payment_method = NULL,",
        "      transaction_id = NULL",
        "  WHERE invoice_number = 'APX-2026-TEST1';",
        "",
        "-- Reopen all escalations",
        "UPDATE escalations",
        "  SET resolved     = FALSE,",
        "      resolved_at  = NULL",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
    ])

    pdf.h3("Reset for Flow E only  (after Flow D, before testing payment)")
    pdf.code_block([
        "-- Only reset invoice payment fields",
        "UPDATE invoices",
        "  SET status = 'unpaid', amount_paid = 0, paid_at = NULL,",
        "      payment_method = NULL, transaction_id = NULL",
        "  WHERE invoice_number = 'APX-2026-TEST1';  -- or use actual number from Flow D",
        "",
        "-- Reset lead stage back to Payment Pending",
        "UPDATE leads",
        "  SET pipeline_stage = 'Payment Pending', closed_won_at = NULL",
        "  WHERE id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
        "",
        "-- Reopen escalations",
        "UPDATE escalations SET resolved = FALSE, resolved_at = NULL",
        "  WHERE lead_id = '6b1761d9-9766-4455-99f4-5a47b0312247';",
    ])

    pdf.h3("Check Current State")
    pdf.code_block([
        "SELECT l.pipeline_stage, l.invoice_number,",
        "       q.status AS quote_status,",
        "       i.status AS invoice_status, i.amount_paid, i.paid_at,",
        "       COUNT(e.id) FILTER (WHERE e.resolved = FALSE) AS open_escalations,",
        "       COUNT(a.id) AS activity_entries",
        "FROM leads l",
        "LEFT JOIN quotes q     ON q.lead_id = l.id",
        "LEFT JOIN invoices i   ON i.lead_id = l.id",
        "LEFT JOIN escalations e ON e.lead_id = l.id",
        "LEFT JOIN activity_log a ON a.lead_id = l.id",
        "WHERE l.id = '6b1761d9-9766-4455-99f4-5a47b0312247'",
        "GROUP BY l.pipeline_stage, l.invoice_number, q.status,",
        "         i.status, i.amount_paid, i.paid_at;",
    ])

    pdf.h3("Supabase Access")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.multi_cell(0, 6,
        "Project URL: https://ioulhoifgcznyezofywb.supabase.co\n"
        "SQL Editor: Supabase Dashboard -> SQL Editor -> New Query\n"
        "Table Editor: Dashboard -> Table Editor (for quick inspection)\n\n"
        "All SQL above is safe to run multiple times. UPDATE on an already-reset row is a no-op.")


# ======================================================================== MAIN
def main():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    pdf.cover()
    add_toc(pdf)
    add_variables_page(pdf)
    add_flow_a(pdf)
    add_flow_b(pdf)
    add_flow_c(pdf)
    add_flow_d(pdf)
    add_flow_e_manual(pdf)
    add_flow_e_stripe(pdf)
    add_db_reference(pdf)

    pdf.output(OUTPUT)
    print(f"PDF written to: {OUTPUT}")


if __name__ == "__main__":
    main()
