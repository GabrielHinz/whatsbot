# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------
WhatsApp Bot Project

Description:
This project implements a WhatsApp bot using the Selenium WebDriver.
The bot is designed to automate various interactions on the WhatsApp
platform, such as authenticating, opening contacts, reading messages,
and sending messages.

Features:
- Authenticate: Log in to the WhatsApp platform using credentials
  or authentication tokens.
- Open Contact: Navigate to a specific contact or group chat to
  perform actions like reading and sending messages.
- Read Message: Retrieve and parse incoming messages from contacts
  or groups for further processing or analysis.
- Send Message: Send text messages, images, files, or emojis to
  individual contacts or groups.

Dependencies:
- Selenium WebDriver: Used for browser automation.

---------------------------------------------------------------
Credits:

Author: 
    Gabriel Hinz

Website:
    https://gabriel.legendproject.com.br
    
Contact: 
    Email: gabriel@legendproject.com.br
---------------------------------------------------------------
"""
import re
import time
import openai

from bot import WhatsBot


def ask_chatgpt(question: str) -> str:
    """
    Sends a question to the OpenAI Chat API and returns the response.

    Parameters:
    - question (str): The question to ask the language model.

    Returns:
    - answer (str): The response from the language model.

    Raises:
    - requests.exceptions.RequestException: If there is an error making the API request.

    Example:
    question = "What is the capital of France?"
    response = ask_chatgpt(question)
    print(response)
    """
    # Insert your OpenAI api key
    openai.api_key = "" 

    # Sending the question to OpenAI
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=question,
            max_tokens=60
        )

        # Returning the response
        answer = response.choices[0].text.strip()
    
    except Exception as er:
        print("There was an error processing your request", er)
        answer = "I couldn't get your answer."
    
    return answer


def start_bot() -> None:
    """
    Starts the bot.

    This function initializes the bot and performs necessary setup operations 
    to start it.

    Parameters:

    Returns:
    - None

    Example:
    start_bot()
    Bot started successfully.
    """
    # Starting a new bot and authenticate.
    bot = WhatsBot(headless=False)
    bot.authenticate()

    # Selecting the contact to talk
    contact = input("Which contact do you want to open? ")

    # Check if contact exists.
    if bot.open_contact(contact):
        bot.send_messages("Hello, i'm a Whatsapp Bot")

        # Inifity loop to check the last messages)
        while True:
            last_msg = bot.last_message()

            # Creating the action calls
            bot_call_start = re.match(r"^/chatgpt\s(.*)$", last_msg)
            bot_call_help = re.match(r"^/help", last_msg)
            bot_call_stop = re.match(r"^/quit", last_msg)

            # Calling the chatgpt ask function and sending the answer
            if bot_call_start:
                question = ask_chatgpt(bot_call_start.group(1))
                bot.send_messages(question)

            # Exiting the program
            elif bot_call_stop:
                bot.quit_driver()
                break

            # Show the help message
            elif bot_call_help:
                bot.send_messages(
                    "\n*/chatgpt* _your question_ -> Asking to ChatGPT" \
                    "\n*/quit* -> Finish the Bot "\
                    "\n*/help* -> Help commands"
                )

            # Sleep
            time.sleep(2)
        
    else:
        print("Cant find the contact.")


def main():
    """
    Starts the bot with chatgpt integration.
    """
    start_bot()


if __name__ == '__main__':
    main()