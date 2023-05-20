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
from bot import WhatsBot


def send_messages_to_contact() -> None:
    """
    Opens a contact and sends a message in a loop.

    This function opens a contact and repeatedly sends a message to that contact.
    The function runs in an infinite loop and does not take any arguments or return any values.

    Note: Use with caution as this function will continuously send messages until manually stopped.

    Args:
        bot (WhatsBot): WhatsBot object 

    Example:
        - Open a contact named 'John'
        - Send a message 'Hello, how are you?' to 'John'
        - Repeat the above step indefinitely until manually stopped
    """
    # Starting a new bot object
    bot = WhatsBot(headless=False)  # set headless to True to hide the webriver
    bot.authenticate()

    # Selecting the contact to talk
    contact = input("Which contact do you want to open? ")

    # Checking if contact exists
    if bot.open_contact(contact):
        
        # Infinity loop for send message
        while True:
            message = input("Type your message (Type !quit to exit) ")

            # quit the program
            if message == '!quit':
                bot.quit_driver()
                break

            # Send the message
            bot.send_messages(message)
    else:
        # if application does not find the contact
        print("Contact not found")


def main():
    """
    This code has some examples of how to use the bot.

    """
    # Starts the first example
    send_messages_to_contact()


if __name__ == '__main__':
    main()
