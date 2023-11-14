import requests
import os

def main():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

    while True:
        message = input("What would you like to say? (Type 'again' to refresh, 'exit' to clear file and end): ")

        if message.lower() == 'exit':
            # Clear the file by sending a special request to the server
            clear_file()
            break
        elif message.lower() == 'again':
            # Display messages from the server and clear the terminal
            get_and_display_messages()
            clear_terminal()
        else:
            # Post the message to the server with the name
            post_message(name, message)
            # Clear the terminal and display messages from the server
            clear_terminal()
            get_and_display_messages()

def post_message(name, message):
    url = "https://upbeatclosedcore.gilpinfamily.repl.co/"
    data = f'{name}: {message}\n'
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Message posted successfully")
    else:
        print(f"Failed to post message. Status code: {response.status_code}")

def get_and_display_messages():
    url = "https://upbeatclosedcore.gilpinfamily.repl.co/"
    response = requests.get(url)

    if response.status_code == 200:
        messages = response.text.split('\n')
        print("Messages from the server:")
        for message in messages:
            if message.strip():
                print(message.strip())
    else:
        print(f"Failed to retrieve messages. Status code: {response.status_code}")

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def clear_file():
    url = "https://upbeatclosedcore.gilpinfamily.repl.co/clear"
    response = requests.post(url)

    if response.status_code == 200:
        print("File cleared successfully")
    else:
        print(f"Failed to clear file. Status code: {response.status_code}")

if __name__ == "__main__":
    main()

