from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch, json

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa").to(device)

def parse_invoice_donut(image_path):
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)

    task_prompt = "<s_docvqa><s_question>Extract invoice fields<s_answer>"
    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids.to(device)

    output_ids = model.generate(pixel_values, decoder_input_ids=decoder_input_ids, max_length=512)
    result = processor.batch_decode(output_ids, skip_special_tokens=True)[0]
    result = result.replace(task_prompt, "").strip()

    try:
        return json.loads(result)
    except:
        return result
