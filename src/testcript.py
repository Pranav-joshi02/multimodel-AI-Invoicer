from ocr_reader import extract_text
from text_qa import answer_from_text

text = extract_text("../demos/sample_inputs/invoice1.jpg")

print("Invoice No:", answer_from_text(text, "What is the invoice number?"))
print("Total Amount:", answer_from_text(text, "What is the total?"))
print("Date:", answer_from_text(text, "What is the date of issue?"))
