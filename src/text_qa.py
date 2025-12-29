from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_from_text(text, question):
    return qa_pipeline({
        'context': text,
        'question': question
    })['answer']
