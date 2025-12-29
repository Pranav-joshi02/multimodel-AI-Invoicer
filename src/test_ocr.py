from ocr_reader import extract_text

images = [
    "../demos/sample_inputs/invoice1.jpg",
    "../demos/sample_inputs/invoice2.jpg",
    "../demos/sample_inputs/invoice3.jpg",
    "../demos/sample_inputs/invoice4.jpg",
]

for path in images:
    print("\nIMAGE:", path)
    text = extract_text(path)
    print("Extracted Text:\n", text[:500])  # print first 500 characters
