import re

def extract_items(text):
    lines = text.split("\n")
    items = []
    capture = False

    for line in lines:
        # Start capturing after ITEMS title
        if re.search(r"\bITEMS\b", line, re.I):
            capture = True
            continue
        if capture and re.search(r"\bSUMMARY\b", line, re.I):
            break
        
        # detect item lines starting like "1." or "2."
        if capture and re.match(r"^\s*\d+\.", line.strip()):
            cleaned = re.sub(r"\s{2,}", " ", line).strip() # normalize spaces
            parts = cleaned.split(" ")

            # last 4 columns ALWAYS qty net vat gross
            qty = parts[-4]
            net = parts[-3]
            vat = parts[-2]
            gross = parts[-1]
            item_name = " ".join(parts[1:-4])

            items.append({
                "item_name": item_name,
                "qty": qty,
                "net_price": net,
                "vat": vat,
                "gross_price": gross
            })

    return items
