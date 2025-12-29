import re

def extract_invoice_fields(text):
    invoice_no = re.search(r"Invoice\s*no[:\-]?\s*(\d+)", text, re.I)
    date = re.search(r"Date(?:\s*of\s*issue)?[:\-]?\s*([\d\/\.-]+)", text, re.I)

    # match final total in summary table
    total = re.search(r"Total\s*[$€₹]?\s*([\d\.,]+)", text, re.I)
    
    return {
        "invoice_no": invoice_no.group(1) if invoice_no else None,
        "date": date.group(1) if date else None,
        "total": total.group(1) if total else None
    }
