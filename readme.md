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
![ask](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2QzZTI3MzI0Yzk3ZDRjZGM2OWJlY2Q4ODY4ZTljMzM4MzQzYjRmZiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/m97AvsRoemkj3oQ34b/giphy.gif)
```
╰─> ask "What is the meaning of life?" 
As an AI language model, I do not have personal beliefs or opinions, but the meaning of life is a philosophical question that has been debated for centuries. Some people believe that the meaning of life is to seek happiness, others believe it is to fulfill a certain purpose or destiny, while others believe it is to find spiritual enlightenment or connection with a higher power. Ultimately, the meaning of life is subjective and can vary from person to person.
```

### To have a chat with Chat GPT
![chat](https://user-images.githubusercontent.com/41730180/234635376-8a31ace3-7cef-41a3-a191-29b79563981b.gif)

```
╰─> chat            
🤖: Ask your question please
🐵: who is the oldest man to ever live on earth
🤖: The oldest man to ever live on earth, according to the Guinness World Records, was Jeanne Calment from France, who lived to be 122 years and 164 days old.
🐵: what about from the bible
🤖: The Bible records several individuals who lived to be very old, but their exact ages are not specified. The oldest recorded age in the Bible is that of Methuselah, who lived to be 969 years old (Genesis 5:27). However, it is important to note that the ages recorded in the Bible are often symbolic and not meant to be taken literally.
🐵: exit
saving data to ./convos/2023-04-26|17:45:01.941006.json
```
note that you have to type exit or quit inorder to safley exit from the console application while still saving the record data.

### To load a previous conversation from a JSON file
![chat-load](https://user-images.githubusercontent.com/41730180/234635496-22147696-690b-4e47-9a46-d47d87b1be90.gif)

```
╰─> chat --load "2023-04-26|17:45:01.941006.json"
Success Data Loaded Succesfully !!!
🤖: Ask your question please
🐵: what were we talking about
🤖: You asked about the oldest man to ever live on earth, and I provided the answer that the oldest man according to the Guinness World Records was Jeanne Calment from France, who lived to be 122 years and 164 days old.
🐵: is that only it ?
```
