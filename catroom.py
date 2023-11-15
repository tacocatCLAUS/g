import requests
import os
import base64
import codecs
import time

def main():
    name = input("Enter your name: ")
    print(f"Welcome, {name}! To...")
    time.sleep(2)
    print("╱╱╱╭━━━╮╱╱╭━━━┳━━━╮ ")
    print("╱╱╱┃╭━╮┃╱╱┃╭━╮┃╭━╮┃ ")
    print("╭━━┫┃┃┃┣╮╭╋╯╭╯┃╰━╯┃ ")
    print("┃╭━┫┃┃┃┃╰╯┣╮╰╮┃╭╮╭╯ ")
    print("┃╰━┫╰━╯┣╮╭┫╰━╯┃┃┃╰╮ ")
    print("╰━━┻━━━╯╰╯╰━━━┻╯╰━╯ ")
    print("Cover your fingerprint/tracks. Easy, Encrypted, 𝕊𝔼ℂ𝕌ℝ𝔼.")

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
            # Encode the message with base64 and apply ROT13
            encoded_message = encode_message(message)
            # Post the encoded message to the server with the name
            post_message(name, encoded_message)
            # Clear the terminal and display messages from the server
            clear_terminal()
            get_and_display_messages()

def encode_message(message):
    # Encode with base64 and add padding
    encoded_message = base64.b64encode(message.encode()).decode() + '==='
    # Apply ROT13
    encoded_message_rot13 = codecs.encode(encoded_message, 'rot_13')
    return encoded_message_rot13

def decode_message(encoded_message_rot13):
    # Reverse ROT13
    decoded_message_base64 = codecs.decode(encoded_message_rot13, 'rot_13')
    
    # Calculate the required padding
    padding = '=' * (4 - (len(decoded_message_base64) % 4))
    
    # Add padding, decode base64, and then decode to UTF-8
    decoded_message = base64.b64decode(decoded_message_base64 + padding).decode('utf-8', 'ignore')
    return decoded_message

def post_message(name, message):
    # Use a different separator to avoid issues during decoding
    separator = '__'
    data = f'{name}{separator}{message}\n'
    
    url = "https://upbeatclosedcore.gilpinfamily.repl.co/"
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
                # Separate the name and message using the chosen separator
                separator = '__'
                if separator in message:
                    name, encoded_message = message.strip().split(separator, 1)
                    # Decode the message received from the server
                    decoded_message = decode_message(encoded_message)
                    # Adjust the printing format
                    print(f'{name} > {decoded_message}')
                else:
                    print(f"Error: Separator not found in message: {message}")
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

