# AIris
# (Basic) Mac Version. (Pocketsphinx) 
- I wrote this program for testing PocketSphinx and see the differencies with Apple Speech Recognition.

- An Artificial Intelligence Bot written in Python and Rivescript

- It has a command line mode and a speech mode

- For installation see 'requirements.txt'

# Usage:
- Type 'python main0.7.py' in Terminal
- The program asks for your Username (this name will be used to store your variables, ie. name, age, etc.).
- Then choose between command line mode or speech mode.
- Now the bot is ready to accept your input. Your chat history and your variables will be saved in a JSON file, so that once you log back (using the same Username) they will be restored and the bot will know it's you.

# Bot's knowledge
Inside the 'brain' folder you can customize the bot's knowledge and actions that correspond to your input.
- Most of the files in this folder are 'default', i just copied and pasted them, i only edited the 'begin' file so that it introduces to a new user asking for his name. I created the files 'system_functions.rive' and 'topics.rive'
- The basics system actions are controlling the input and output volume, empty trash, enable/disable wifi, list the wifi connection available.

- Please go to 'https://www.rivescript.com/docs/tutorial' for more info about Rivescript
