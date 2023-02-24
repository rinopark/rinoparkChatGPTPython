import os
import openai
import datetime

# authentication
openai.organization = "org-8wjsJHez1shnr0NMo5pLMw1F"
openai.api_key  = "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"

# check models
modelList = openai.Model.list()
print("================================================\r\n")
print(modelList)
print("================================================\r\n")

# initialize
loopFlag = "Y"
prompt = ""
currentTime = datetime.datetime.now()
print("================================================\r\n")
print(currentTime)
print("================================================\r\n")

# Set up the model
model_engine = "text-davinci-003"

# get input from user
greetingMessage = ""
if currentTime.hour < 12:
    greetingMessage = "Good morning"
elif 12 <= currentTime.hour < 18:
    greetingMessage = "Good afternoon"
else:
    greetingMessage = "Good evening"

print(f"ChatGPT> {greetingMessage} sir.")



response = openai.Image.create(
  prompt="man's face.",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)

# while loopFlag == "Y":
#     prompt = input("you> ")
#     if prompt.lower() == "quit" or prompt == "종료":
#         loopFlag = "F"
#     else:
#         # Generate a response
#         completion = openai.Completion.create(
#             engine=model_engine,
#             prompt=prompt,
#             max_tokens=1024,
#             n=1,
#             stop=None,
#             temperature=0.5,
#             #top_p=1,
#             #frequency_penalty=2,
#             #presence_penalty=0,
#         )
#         # display response from ChatGPT
#         response = completion.choices[0].text
#         print(f"ChatGPT> {response} \n")

