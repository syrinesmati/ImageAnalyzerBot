import base64
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables.")


def process_image(image_path, query):
    try:
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        try:
            image = Image.open(io.BytesIO(img_bytes))
            image.verify()  # Verify that it is, in fact an image
        except Exception as e:
            logger.error("invalid image format: %s", e)
            return None
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "query"},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
                ]
            }
        ]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": messages
        }
        
        def make_api_request(model):
            response=requests.post(
                GROQ_API_URL,
                json={
                    "model": model,
                    "messages": messages,
                    "max_tokens": 1000
                },
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout=30
            )
            return response
        
        llama_11b_response = make_api_request("meta-llama/llama-4-scout-17b-16e-instruct")
        llama_90b_response = make_api_request("meta-llama/llama-4-maverick-17b-128e-instruct")
        
        responses = {}
        for model, response in [("llama-11b", llama_11b_response), ("llama-90b", llama_90b_response)]:
            if response.status_code == 200:
                result = response.json()
                answer = result['choices'][0]['message']['content']
                logger.info(f"Processed response from {model} API : {answer}")
                responses[model] = answer
            else:
                logger.error("Error from %s: %s", model, response.text)
                responses[model] = f"Error from {model} API: {response.status_code}"
        
        return responses
                
    except Exception as e:
        logger.error("Error processing image: %s", e)
        return None
     
    
if __name__ == "__main__":
    image_path = "test1.png"  # Replace with your image path
    query = "What is in this image?"
    result = process_image(image_path, query)
    print(result)