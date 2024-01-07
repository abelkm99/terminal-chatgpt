from collections import deque
from datetime import datetime
import json
import os

from openai import Stream

from colors import COLORS

PATH = os.path.expanduser("~/Documents")
os.chdir(path=PATH)


def print_response(response: Stream, messages: list[dict]):
    data = []
    dq = deque()
    for chunk in response:
        res = chunk.choices[0].delta
        if res.content:
            res = res.content
            for c in res:
                dq.append(c)
            data.append(res)
            temp = []
            while " " in dq:
                temp.append(dq.popleft())
            temp = "".join(temp)
            print(f"{COLORS.GREEN}{temp}", end="", flush=True)

    temp = []
    while dq:
        temp.append(dq.popleft())
    temp = "".join(temp)
    print(f"{COLORS.GREEN}{temp}", end="", flush=True)

    print()
    messages.append({"role": "assistant", "content": "".join(data)})


def create_folder():
    folder_name = "convos"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def write_messages_to_json(messages, json_name, is_exit=False):
    if len(messages) == 0:
        return

    create_folder()
    json_name = (
        "./convos/" + "|".join(str(datetime.now()).split()) + ".json"
        if not json_name
        else "./convos/" + json_name
    )
    if is_exit:
        print("saving data to " + json_name)
    with open(json_name, "w") as f:
        json.dump(messages, f, indent=2)


def validate_json(file_name):
    path = "./convos/" + file_name
    if not os.path.exists(path):
        return (False, "File name doesn't exists", [])
    try:
        data = None
        # load the data
        with open(path, "r") as f:
            data = f.read()
        data = json.loads(data)
        # validate that each row has the specified key and value
        i = 0
        for turn in data:
            keys = turn.keys()
            if (
                "role" in keys and "content" in keys and turn["role"] == "user"
                if i % 2 == 0
                else "assistant"
            ):
                pass
            else:
                return (False, "INVALID FORMAT", [])
            i += 1
        return (True, "Data Loaded Succesfully", data)
    except Exception as e:
        return (False, str(e), [])
