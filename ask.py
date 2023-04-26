import sys
from utils import print_response
import os
import openai
from dotenv import load_dotenv
from utils import COLORS

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = " ".join(sys.argv[1:]).strip()

if len(prompt):

  messages = []

  messages.append({
      "role":"user",
      "content": prompt
  })

  response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=0,
        messages = messages,
        stream=True
    )
  print_response(response,messages)
else:
  print(f"{COLORS.RED}Error No question is Asked!!! {COLORS.ENDC}")