import argparse
from datetime import datetime
import os
import openai
from dotenv import load_dotenv
from colors import COLORS
from utils import print_response, validate_json, write_messages_to_json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.Client()

parser = argparse.ArgumentParser()
parser.add_argument("--load", help="Enter the name of previous conversation")
args = parser.parse_args()

messages = []

json_name = args.load if args.load else "|".join(str(datetime.now()).split()) + ".json"
print("session saved as: ", json_name)

if args.load:
    res, response_message, data = validate_json(args.load)
    if res:
        messages = data
        print(f"{COLORS.GREEN}Success {response_message} !!! {COLORS.ENDC}")
    else:
        print(
            f"{COLORS.RED}Error {response_message}, continuing with empty data!!! {COLORS.ENDC}"
        )

print(f"{COLORS.RED}🤖{COLORS.ENDC}: Ask your question please")
exits = ["quit", "exit"]
prompt = ""
while True:
    prompt = input(f"{COLORS.BLUE}🐵{COLORS.ENDC}: ")
    if prompt.lower() in exits:
        write_messages_to_json(messages, json_name, True)
        break
    messages.append({"role": "user", "content": prompt})

    print(f"{COLORS.YELLOW}🤖{COLORS.ENDC}:", end=" ", flush=True)

    stream_response: openai.Stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=messages,
        stream=True,  # this time, we set stream=True
    )
    print_response(stream_response, messages)
    # TODO find a better way to save only the new response
    write_messages_to_json(messages, json_name=json_name)
