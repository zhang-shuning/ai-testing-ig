'''
Main file, just testing for now
This code was/is copy and pasted boiler plate
'''
import os
import base64
from openrouter import OpenRouter
import io
from PIL import Image

RUN_AI = True

def encode_image(path):
    #AI generated function
    #Clears metadata
    with Image.open(path) as img:
        with io.BytesIO() as buffer:
            img.getexif().clear()
            img.save(buffer, format="JPEG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")

image = r"C:\Users\user\Desktop\Python\ai-testing-ig\images_to_use\Abyssinian_1.jpg"
base64_image = encode_image(image)
data_url = f"data:image/jpeg;base64,{base64_image}"

messages = [
    {
        "role": "system",
        "content": "You will be shown an image of a cat or dog, your job is to respond with only the breed of the animal with no capitals."
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What's in this image?"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": data_url
                }
            }
        ]
    }
]

if __name__ == "__main__":
    print(len(base64_image))
    if RUN_AI:
        client = OpenRouter(
            api_key = os.environ["API_KEY"],
            server_url = os.environ["URL"]
        )

        response = client.chat.send(
            model="google/gemini-3-flash-preview",
            messages=messages
        )

        print(response.choices[0].message.content)
