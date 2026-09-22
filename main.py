'''
Main file, just testing for now
This code was/is copy and pasted boiler plate
'''
import os
import base64
from openrouter import OpenRouter

RUN_AI = True

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

image = r"C:\Users\user\Pictures\tank.png"
base64_image = encode_image(image)
data_url = f"data:image/jpeg;base64,{base64_image}"

messages = [
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
