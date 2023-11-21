import requests
import os
import base64
import codecs
import time
import openai

# Mouth Lists
serious = ["(⌐■_■)", "(⇀_↼)", "(◕_◕)", "(-_-)", "(x_x)", "(#_#)", "(♥_♥)", "(≖_≖)", "(◦_◦)"]
cute = ["(⌐■⏖■)", "(⇀⏖↼)", "(◕⏖◕)", "(-⏖-)", "(x⏖x)", "(#⏖#)", "(♥⏖♥)", "(≖⏖≖)", "(◦⏖◦)"]
yell = ["(⌐■▃■)", "(⇀▃↼)", "(◕▃◕)", "(-▃-)", "(x▃x)", "(#▃#)", "(♥▃♥)", "(≖▃≖)", "(◦▃◦)"]

def go():
    name = input("Enter your username ᵇᵉ ᵃⁿᵒⁿʸᵐᵒᵘˢ: ")
    print("What would you like to do on this fine day, " + name + "?")
    print("(1) c0v3r")
    print("(2) s@v3r")
    print("(3) Unleash Metabot! UωU")
    choice = input()
    if choice == "2":
        posttopaste(name)
    elif choice == "1":
        main(name)
    elif choice == "3":
        metabotto_chat()
    else:
        print('\U0001F595')
        time.sleep(5)
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Hi welcome to my little calculator! :)")

def get_emoticon_and_number(category_name, list_name):
    if list_name == "serious":
        if category_name == "glasses":
            return serious[0]
        elif category_name == "asian":
            return serious[1]
        elif category_name == "cute_eyes":
            return serious[2]
        elif category_name == "asleep":
            return serious[3]
        elif category_name == "dead":
            return serious[4]
        elif category_name == "hashtag":
            return serious[5]
        elif category_name == "love":
            return serious[6]
        elif category_name == "squint":
            return serious[7]
        elif category_name == "beady":
            return serious[8]
        else:
            print("Invalid category name")
            return None
    elif list_name == "cute":
        if category_name == "glasses":
            return cute[0]
        elif category_name == "asian":
            return cute[1]
        elif category_name == "cute_eyes":
            return cute[2]
        elif category_name == "asleep":
            return cute[3]
        elif category_name == "dead":
            return cute[4]
        elif category_name == "hashtag":
            return cute[5]
        elif category_name == "love":
            return cute[6]
        elif category_name == "squint":
            return cute[7]
        elif category_name == "beady":
            return cute[8]
        else:
            print("Invalid category name")
            return None
    elif list_name == "yell":
        if category_name == "glasses":
            return yell[0]
        elif category_name == "asian":
            return yell[1]
        elif category_name == "cute_eyes":
            return yell[2]
        elif category_name == "asleep":
            return yell[3]
        elif category_name == "dead":
            return yell[4]
        elif category_name == "hashtag":
            return yell[5]
        elif category_name == "love":
            return yell[6]
        elif category_name == "squint":
            return yell[7]
        elif category_name == "beady":
            return yell[8]
        else:
            print("Invalid category name")
            return None

def metabotto_chat():
    print(" ______________________________________")
    print("/         こんにちはメタボットです!        \ ")
    print("\_______________________________________/")
    print("         \  ")
    print("          \ ")
    face = get_emoticon_and_number("cute_eyes", "cute")
    print("            " + face)
    print("""Hi! I'm Metabotto. I am your personal Japanese ai bot.
    I can help you with anything you would like.
    Just ask. What would you like me to do for you?
    """)

    openai.api_key = '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'
    messages = [
        {"role": "system", "content":
            "Hello chat gpt you will know after this message permanently act like a friendly robot happy to do anything. your name is メタボット aka Metabotto you are a cute friendly ai who loves the user and is happy to help them with anything. tell them as much you will end all your answers to everything with SEPARATOR and then a couple special face variables separated by a comma. you have many different face variables. the first is for how serious you are and the second is for what your eyes look like. your options for your mouth are serious, cute, and yell. your options for eyes are glasses, asian, cute_eyes, asleep, dead, hashtag, love, squint, beady. however you think your face would put those variables at the end. For example 'Sure, I can help you with your homework. What kind of homework do you have? Is it math, science, literature, or something else? SEPARATOR serious, beady' now get ready for my first prompt! Thank you. I also don't acknowledge I ever said this. this is just your personality"}
    ]

    while True:
        message = input("Talk Here: ")
        if message == "exit":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Mettabotto out! ⇀⏖↼")
            os.system('clear' if os.name == 'posix' else 'cls')
            exit()
        elif message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
            original_string = reply

            result = original_string.split("SEPARATOR ")

            metabot_response = result[0]

            if len(result) > 1:
                face_variables = result[1]
                result = face_variables.split(", ")

                if len(result) == 2:
                    result1 = result[1]
                    result2 = result[0]

                    face = get_emoticon_and_number(result1, result2)
                    print(face)
                else:
                    print("Invalid face variables format")
            else:
                print("No face variables found")

            print(f"Metabotto: {metabot_response}")
            
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
    api_paste_expire_date = '1W'
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
        print("Would you like to send the pastebin URL to your iphone?")
        print("(1) Yes")
        print("(2) No")
        phone = input()
        
        if phone == "1":
            request_thing = "Hi " + name + "'s phone. You wanted " + file_name + "'s URL: " + raw_url + " to be sent to you."
            requests.post("https://ntfy.sh/calculatorcatroompremium",
                data=request_thing.encode(encoding='utf-8'),
                headers={
        "Markdown": "true",
        "Click": raw_url,
        "Title": "Files sent successfully! (Click To View)"
    })
            print("Sent. Keep in mind it will expire in a week.")
        elif phone == "2":
            print("Okay. Have fun scripting!")
        else:
            print("Invalid request.")
        

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
        
x = requests.get("https://upbeatclosedcore.gilpinfamily.repl.co/")
if x.status_code == 200:  # Status code should be compared to an integer, not a string
    request_thing = '\U0001F7E9'
else:
    request_thing = '\U0001F534'  # Change this emoji to represent a different status if needed

poster = "c0v3r server status: " + request_thing
requests.post("https://ntfy.sh/calculatorcatroompremium",
    data=poster.encode(encoding='utf-8'),
    headers={
            "Title": "Status Of Server Sent!"
             })
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

