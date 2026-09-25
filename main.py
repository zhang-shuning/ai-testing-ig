'''
Main file, just testing for now
This code was/is copy and pasted boiler plate
'''
import os
import base64
import pathlib
from openrouter import OpenRouter
import io
from PIL import Image

RUN_AI = True

RUN = "Control"

current_num_path = pathlib.Path(r'data\current_num.dat')
images = pathlib.Path("images_to_use")
files = [item for item in images.iterdir() if item.is_file()]
result_list = []

def get_name(file:pathlib.Path):
    '''Returns the name of the file'''
    cur_name = file.name
    for j in range(len(cur_name)-1, -1, -1):
        if cur_name[j] == '_':
            return cur_name[0:j].lower()

def encode_image(path):
    '''AI generated function'''
    #Clears metadata
    with Image.open(path) as img:
        with io.BytesIO() as buffer:
            img.getexif().clear()
            img.save(buffer, format="JPEG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")

def write_results(results):
    num = update_get_current_num()
    with open(current_num_path.parent/f"result{num}.txt", "a") as f:
        for i in results:
            f.write(str(i)+'\n')

def update_get_current_num():
    current_num_path.parent.mkdir(parents=True, exist_ok=True)
    current_num_path.touch()
    with open(current_num_path, "r") as f:
        num_string = f.read()
        if num_string.isdigit():
            num = str(int(num_string)+1)
        else:
            print("the data file is not a number")
            print("Remaking file at 2...")
            num = '2'
    with open(current_num_path, "w") as f:
        f.write(num)
        return int(num)-1

def main():
    count = 0
    name = ""
    file_count = len(files)
    for file in files:
        count += 1
        name = get_name(file)
        print(f"Testing file {file} ({count}/{file_count})")

        base64_image = encode_image(file)
        data_url = f"data:image/jpeg;base64,{base64_image}"

        messages = [
            {
                "role": "system",
                "content": "You will be shown an image of a cat or dog, your job is to respond with only the breed of the animal in lowercase."
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

        if RUN_AI:
            try:
                client = OpenRouter(
                    api_key = os.environ["API_KEY"],
                    server_url = os.environ["URL"]
                )

                response = client.chat.send(
                    model="google/gemini-3-flash-preview",
                    messages=messages
                )
            except Exception as e:
                print(f"There was an exception {e}")
                print("Writing results...")
                write_results(result_list)
                return
            result_list.append((count, name, response.choices[0].message.content))
    write_results(result_list)

    


if __name__ == "__main__":
    main()
