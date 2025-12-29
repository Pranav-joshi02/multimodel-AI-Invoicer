import streamlit as st
from PIL import Image
import torch

# --- Import project modules ---
from ocr_reader import extract_text
from extract_info import extract_invoice_fields
from text_sentiment import get_sentiment
from caption_generator import generate_caption
from text_qa import answer_from_text
from extract_table import extract_items
from invoice_donut import parse_invoice_donut

st.title("📄 AI Invoice Analyzer (Vision + OCR + Donut + QA)")
st.write("Upload an invoice to extract details automatically.")

uploaded_file = st.file_uploader("📎 Upload Invoice Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load Image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

    # Save temporarily
    file_path = "temp_invoice.jpg"
    image.save(file_path)

    # ------------------- DONUT STRUCTURED EXTRACTION -------------------
    st.subheader("🤖 Donut AI Extraction (Structured Parsing)")
    donut_data = parse_invoice_donut(file_path)
    st.json(donut_data)

    # ------------------- OCR TEXT EXTRACTION -------------------
    st.subheader("🔍 OCR Extracted Text")
    text = extract_text(file_path)
    st.text_area("Extracted Text", text, height=200)

    # ------------------- BASIC FIELD EXTRACTION -------------------
    st.subheader("📌 Invoice Details (Regex Based)")
    info = extract_invoice_fields(text)
    st.json(info)

    # ------------------- PURCHASED ITEMS (Regex Table) -------------------
    st.subheader("🛒 Purchased Items")
    items = extract_items(text)

    if items:
        st.table(items)
    else:
        st.warning("❌ No structured items detected by regex.\nDonut extraction above may contain them.")

    # ------------------- CAPTION -------------------
    st.subheader("📝 Image Caption")
    caption = generate_caption(file_path)
    st.write(caption)

    # ------------------- SENTIMENT -------------------
    st.subheader("💬 Sentiment")
    sentiment = get_sentiment(text)
    st.json(sentiment)

    # ------------------- USER Q/A -------------------
    st.subheader("❓ Ask invoice a question")
    user_q = st.text_input("Ask (e.g., 'What is total amount?' or 'Who is seller?')")

    if user_q:
        answer = answer_from_text(text, user_q)
        st.success(f"Answer: {answer}")
