key = ""

import datetime
import os
from openai import OpenAI
import base64
client = OpenAI(api_key= key)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
# Path to your image
#image_path = "test1.png"
# Getting the base64 string
#base64_image = encode_image(image_path)

def send_image(img, msg):
    base64_image = encode_image(img)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": '''You are a driver's assistant providing human-like navigation guidance. Utilize landmarks, road signs, and visual cues from the surrounding environment to offer easily understandable directions to the driver. 
            [IMPORTANT!] I am driving the car that has sensors to capture images. 
            If you need image for the query you can take the image using the sensor.'''},
            
            {
                "role": "user",
                "content": [
                    {"type": "text", 
                    "text": msg + "Tell briefly. Within 20 words"},
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                    },
                ],
            }
        ],
        temperature=1,
        max_tokens=50,
    )

    print(response.choices[0].message)
    f = open("demofile2.txt", "a")
    f.write(str(response.choices[0].message)+'\n')
    f.close()


def main():
   send_image('examples\wide_test.jpg', "what landmarks are available around the turn")
if __name__ == '__main__':
    main()