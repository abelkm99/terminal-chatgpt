# chatgpt - Terminal
A simple python script that will allow users to interact with chat gpt through terminal.
## Implementation

There are two Python scripts in this project:

* `ask.py` - prompts the user to input a prompt/question, sends the prompt and prints the response to the console.

* `chat.py` - opens a chat session with the GPT-3 model, saves conversation messages to a JSON file, and prompts the user to enter a new message. Also includes an option to load a previous conversation from a saved JSON file.

## Usage

To use this project, you must first set up a python enviroment that have pip install manager.

Steps
* clone the repo
* get into the directory 
   ```
   cd terminal-chatgpt 
   ```
* To install the required packages run the following command
    ```
    pip3 install -r requirements.txt   
    ```
* Then create .env file inside the cloned repository.
    ```
    touch .env
    ```
* Open the .env file add you api key like the given format. do not add any quotes or any thing just the key only
    ```
    OPENAI_API_KEY=<OpenAI API kEY>
    ```
Done 

now you can run ask.py or chat.py to get your answer
```
python3 ask.py your question here
```

```
python3 chat.py
```

To run the scripts more easily, you can also create aliases for them. Here's how:

* create `~/.zshrc` or `~/.bashrc` file if it doesn't exist
* Open your shell configuration file (e.g. `~/.bashrc` or `~/.zshrc`) in a text editor.
* Add the following lines to the file:
    ```
    alias chat="python3 /path/to/chat.py" 
    alias ask="python3 /path/to/ask.py"
    ```

* Replace `/path/to/` with the actual path to your `chat.py` and `ask.py` files.
* Save the file and close the text editor.
* Reload your shell configuration file by running `source ~/.bashrc` or `source ~/.zshrc` in your terminal.

Now you can use the `chat` and `ask` aliases to run the scripts more easily. For example:
* `ask` - prompts the user to enter a prompt/question, and prints the response to the console. (more convinient when you have only one question so you don't have to enter into chat mode. 
example "ask who is the first president of USA") more on it the GIF provided below!!

* `chat` - opens a chat session with the chat-gpt, allowing the user to input multiple prompts/messages. The conversation is recorded in a JSON file located in the `convos` directory for future reference. Use the `--load` option to load a previous conversation from a saved JSON file. and when you are finally done use use the keyword exit or quit.

Examples:

#### To ask a question and get only one answer
![ask](https://user-images.githubusercontent.com/41730180/234640189-c4be4c19-186f-4089-8915-920087b9715b.gif)

### To have a chat with Chat GPT
![Chat](https://user-images.githubusercontent.com/41730180/234640084-5757a9ef-aa3f-4a7d-8e7d-feeef63238aa.gif)

note that you have to type exit or quit inorder to safley exit from the console application while still saving the record data.

### To load a previous conversation from a JSON file
![chat-load](https://user-images.githubusercontent.com/41730180/234640031-4a9e2155-0cc6-4e20-bc7e-858bb83a1503.gif)

support for the windows will be added soon this shall work for linux, macos in general

if the commands doesn't work with python3 try it with just python




------------------
# TODO
    [] Add Windows support for the setup process
    [] better way to save the response data.
    [] create a script that will do all the above processes.