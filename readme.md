# chatgpt - Terminal
A simple python script that will allow users to have a chat with chat gpt through terminal
## Implementation

There are three Python scripts in this project:

* `ask.py` - prompts the user to input a prompt/question, sends the prompt to OpenAI's GPT-3 model, and prints the response to the console.

* `chat.py` - opens a chat session with the GPT-3 model, saves conversation messages to a JSON file, and prompts the user to enter a new message. Also includes an option to load a previous conversation from a saved JSON file.

## Usage

To use this project, you must first set up a python environment and install the required dependencies using the `requirements.txt` file. You must also create an OpenAI API key and store it in a `.env` file located in the project root directory. 

* To install the required packages run the following command
    ```
    pip install -r requirements.txt   
    ```
* Then create .env file inside the cloned repository add your api key there.
    ```
    OPENAI_API_KEY=<OpenAI API kEY>
    ```

To run the scripts more easily, you can also create aliases for them. Here's how:

* Open your terminal and navigate to the project directory.
* Open your shell configuration file (e.g. `~/.bashrc` or `~/.zshrc`) in a text editor.
* Add the following lines to the file:
    ```
    alias chat="python /path/to/chat.py" 
    alias ask="python /path/to/ask.py"
    ```

* Replace `/path/to/` with the actual path to your `chat.py` and `ask.py` files.
* Save the file and close the text editor.
* Reload your shell configuration file by running `source ~/.bashrc` or `source ~/.zshrc` in your terminal.

Now you can use the `chat` and `ask` aliases to run the scripts more easily. For example:
* `ask` - prompts the user to enter a prompt/question, and prints the response to the console. (more convinient when you have only one question so you don't have to enter into chat mode. 
example "who is the first president of USA").

* `chat` - opens a chat session with the chat-gpt, allowing the user to input multiple prompts/messages. The conversation is recorded in a JSON file located in the `convos` directory for future reference. Use the `--load` option to load a previous conversation from a saved JSON file. and when you are finally done use use the keyword exit or quit.

Examples:

#### To ask a question and get only one answer
![ask](https://user-images.githubusercontent.com/41730180/234640189-c4be4c19-186f-4089-8915-920087b9715b.gif)

### To have a chat with Chat GPT
![Chat](https://user-images.githubusercontent.com/41730180/234640084-5757a9ef-aa3f-4a7d-8e7d-feeef63238aa.gif)

note that you have to type exit or quit inorder to safley exit from the console application while still saving the record data.

### To load a previous conversation from a JSON file
![chat-load](https://user-images.githubusercontent.com/41730180/234640031-4a9e2155-0cc6-4e20-bc7e-858bb83a1503.gif)
