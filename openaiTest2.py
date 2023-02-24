# sourcery skip: assign-if-exp, merge-else-if-into-elif, remove-redundant-if
import os
import openai
import datetime
import webbrowser

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

# 1. Text completion, 2. Image generation.
wantTodoWithyou = 1 # Default: is Test completion.
print(f"ChatGPT> {greetingMessage} sir. pls select what you want to do with me sir. 1. Text completion, 2. Image generation.")
prompt = input("your choice.> ")
if prompt == '1':
    wantTodoWithyou = 1
else:
    wantTodoWithyou = 2

while loopFlag == "Y":
    if wantTodoWithyou == 1:
        prompt = input("(Text) you> ")
    else:
        prompt = input("(Image Gen) you> ")
        
    if prompt.lower() == "quit" or prompt == "종료":
        loopFlag = "F"
    else:
        if wantTodoWithyou == 1:
            # Generate a response of text completion.
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
                #top_p=1,
                #frequency_penalty=2,
                #presence_penalty=0,
            )
            # display response from ChatGPT
            response = completion.choices[0].text
            print(f"ChatGPT> {response} \n")
        else:
            # Generate a response of image generation.
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512" # one of ['256x256', '512x512', '1024x1024'] - 'size'
            )
            image_url = response['data'][0]['url']
            webbrowser.open(image_url)