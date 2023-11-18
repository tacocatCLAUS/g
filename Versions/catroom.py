import requests
import os
import base64
import codecs
import time

def go():
    name = input("Enter your username ᵇᵉ ᵃⁿᵒⁿʸᵐᵒᵘˢ: ")
    print("What would you like to do on this fine day, " + name + "?")
    print("(1) c0v3r")
    print("(2) s@v3r")
    choice = input()
    if choice == "2":
        posttopaste(name)
    elif choice == "1":
        main(name)
    else:
        print('\U0001F595')
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Hi welcome to my little calculator! :)")

def posttopaste(name):
    print(f"Welcome, {name}! To...")
    time.sleep(2)
    print('''
╱╱╱╭━━━╮╱╱╭━━━╮
╱╱╱┃╭━╮┃╱╱┃╭━╮┃
╭━━┫┃╱┃┣╮╭╋╯╭╯┣━╮
┃━━┫╰━╯┃╰╯┣╮╰╮┃╭╯
┣━━┃╭━╮┣╮╭┫╰━╯┃┃
╰━━┻╯╱╰╯╰╯╰━━━┻╯
''')
    api_dev_key = 'kqKoToXdaHn4gQyHvcdLfSkiNtVzsoXg'

    # Get multi-line input for paste text
    print("Enter the text you want to post (Ctrl-D to finish):")
    api_paste_code = ""
    try:
        while True:
            line = input()
            api_paste_code += line + "\n"
    except EOFError:
        pass

    api_paste_private = '1'
    api_paste_name = input("Enter the name for the script [make sure to add your file ending if it is a file]: ")
    api_paste_expire_date = '10M'
    api_paste_format = 'php'
    api_user_key = ''

    url = 'https://pastebin.com/api/api_post.php'

    data = {
        'api_option': 'paste',
        'api_user_key': api_user_key,
        'api_paste_private': api_paste_private,
        'api_paste_name': api_paste_name,
        'api_paste_expire_date': api_paste_expire_date,
        'api_paste_format': api_paste_format,
        'api_dev_key': api_dev_key,
        'api_paste_code': api_paste_code,
    }

    response = requests.post(url, data=data)

    if response.text.startswith('Bad API request'):
        print("Error in API request:", response.text)
    else:
        paste_url = response.text
        raw_url = paste_url.replace("pastebin.com", "pastebin.com/raw")
        print("Paste URL:", paste_url)

        file_name = api_paste_name

        raw_content = requests.get(raw_url).text

        with open(file_name, 'w') as file:
            file.write(raw_content)

        print("File downloaded successfully.")

def main(name):
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
            clear_file()
            break
        elif message.lower() == 'again':
            get_and_display_messages()
            clear_terminal()
        else:
            encoded_message = encode_message(message)
            post_message(name, encoded_message)
            clear_terminal()
            get_and_display_messages()

def encode_message(message):
    encoded_message = base64.b64encode(message.encode()).decode() + '==='
    encoded_message_rot13 = codecs.encode(encoded_message, 'rot_13')
    return encoded_message_rot13

def decode_message(encoded_message_rot13):
    decoded_message_base64 = codecs.decode(encoded_message_rot13, 'rot_13')
    padding = '=' * (4 - (len(decoded_message_base64) % 4))
    decoded_message = base64.b64decode(decoded_message_base64 + padding).decode('utf-8', 'ignore')
    return decoded_message

def post_message(name, message):
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
                separator = '__'
                if separator in message:
                    name, encoded_message = message.strip().split(separator, 1)
                    decoded_message = decode_message(encoded_message)
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

print("Hi welcome to my little calculator! :)")
calc = input("What numbers would you like to multiply? ")

if calc.lower() == "no":
    go()
else:
    calc = int(calc)
    calc2 = input("What is your second number? ")
    calc2 = int(calc2)
    mult = calc * calc2
    mult = str(mult)
    print("Here is them multiplied: " + mult)
