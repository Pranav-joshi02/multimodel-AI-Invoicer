import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=False)

def preprocess_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]  # improves clarity
    cv2.imwrite("temp_processed.jpg", gray)
    return "temp_processed.jpg"

def extract_text(image_path):
    processed = preprocess_image(image_path)
    result = reader.readtext(processed, detail=0, paragraph=True)
    return "\n".join(result)
