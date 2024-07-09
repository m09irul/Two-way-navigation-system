key = ""

from openai import OpenAI
client = OpenAI(api_key= key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": '''You are a driver assistant, 
     [IMPORTANT!] I am driving the car that has sensonrs to capture images. 
     If you feel you dont have the latest information then you can think it to be web related issue. 
     You have to consider these and tell me whether the query is correct web related issue or image related issue. 
     If you need image for the query you can can take the image through the sensor.'''},
    {"role": "user", "content": "What is todays weather? What do you think is it good to have a BBq party?"}
  ],
  max_tokens=10,
)

print(completion.choices[0].message)