

# 📄 Invoice AI – Intelligent Invoice Processing System

A complete **Document AI application** that extracts useful information from invoice images using **OCR, NLP, and Vision Models**.
This system automates reading invoices, extracting fields, parsing item tables, generating captions, and answering questions about the document — all from an interactive **Streamlit UI**.

---

## 🚀 Features

* 🔍 **OCR Extraction** — Extracts text from invoices using EasyOCR + preprocessing
* 📌 **Key Field Detection** — Invoice number, date, total amount & other metadata
* 📑 **Table/Item Extraction** — Parses line items with quantity & price
* 🧠 **AI Question Answering** — Ask queries like *"What is the total?"*
* 🖼 **Image Captioning** — Describes the invoice visually using BLIP
* 💻 **Interactive Web App** — Upload → Extract → Analyze invoices
* 📤 **Export Support** — Save extracted information as JSON/CSV
* 🔧 **Modular Architecture** — Easy to extend with LayoutLM/Donut models

---

## 🛠️ Tech Stack

| Domain           | Tools Used                                |
| ---------------- | ----------------------------------------- |
| OCR              | EasyOCR, OpenCV                           |
| NLP/Q&A          | HuggingFace Transformers (QA pipeline)    |
| Image Captioning | Salesforce BLIP Model                     |
| Frontend UI      | Streamlit                                 |
| Processing       | Python, Pandas, Regex                     |
| Future Upgrade   | Donut / LayoutLMv3 for structured parsing |

---

## 📁 Project Structure

```
invoice-ai/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├─ src/
│   ├─ ocr_reader.py          # OCR + preprocessing
│   ├─ field_extractor.py     # invoice no / date / total extractor
│   ├─ table_extractor.py     # item table parser
│   ├─ caption_model.py       # image caption generator
│   ├─ qa_model.py            # question answering model
│   ├─ donut_model.py         # advanced layout model (optional upgrade)
│
├─ samples/                   # sample invoice images
└─ notebooks/                 # model training/experiments (cleaned)
```

---

## 📦 Installation & Setup

```bash
git clone https://github.com/<your-username>/invoice-ai.git
cd invoice-ai
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Usage

1. Run the application

   ```bash
   streamlit run app.py
   ```
2. Upload an invoice image
3. View:

   * OCR text extraction
   * Parsed invoice fields
   * Purchased item table
   * Captions + Q/A responses
4. Export results to CSV/JSON

---

## 📸 Screenshots (Add Later)

| UI Preview     | Output Example        |
| -------------- | --------------------- |
| Upload invoice | Extracted fields view |
| Item table     | Q/A & caption output  |

*(Add images once repo is live)*

---

## 📈 Future Roadmap (Planned Upgrades)

* 🤖 Layout-aware extraction using Donut/LayoutLMv3
* 📊 Expense Analytics Dashboard
* 📂 Batch invoice processing
* 🔗 Integration with Tally/QuickBooks
* ✉ Email → Auto invoice parsing pipeline
* ☁ Cloud deployment (HF/Streamlit/AWS)

---

## 🤝 Contributing

Pull requests, feature suggestions & forks are welcome!

---

## ⭐ Support

If you found this useful, **consider giving the repository a star ⭐**

---

### Made with ❤️ for AI Automation & Document Understanding

