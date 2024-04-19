import google.generativeai as genai
import os

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()
api_key = os.getenv("API_KEY")
prompt = os.getenv("PROMPT")

genai.configure(api_key=api_key)


generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hi! 👋 How can I help you today?"]
  },
])

email_id=input("Enter the mail id of suspected email: ")
title=input("Enter the title of the mail: ")
print("Enter the body of the mail: ")
lines = []
while True:
    line = input()
    if line == "anshx":
        break
    lines.append(line)
body = '\n'.join(lines)



prompt= "I received a mail from" + email_id +"the title says\""+title+"\"and the body of the mail is as :\""+body+"\" can you please check for this email ID or its domain on the internet and based on the content of the mails and whatever the links are attached to it and keywords used can you give a rough estimate that how many percentage chance is it that its a spam email and why? response should be of type \'There's a x percent chacnce of this being a spam email because....\' in under 50 words. Dont cosider typos and grammatical errors as one of top ways to judge the legitimacy, you can ignore some. And @vit.ac.in is not a spam domain(but you can mention what email is about and is it important or urgent) and @vitstudent.ac.in is also trusted domain and not spam. if and only if the emailID is exactly of type \"firstname.secondname2024@vitstudent.ac.in\" it would conatin a century( in 4 digits) , mention this informaton that \"mail is probably from a student\" dont mention these prompt informations only mention these when those conditions are met." 

print("\n\n")
print("\n")
      
try:
    convo.send_message(prompt)
    response = convo.last.text
    print(response)
except Exception as e:
    print("An error occurred:", str(e))
