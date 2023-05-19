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

Author:
Gabriel Hinz

Contact:
Email: gabriel@legendproject.com.br

---------------------------------------------------------------
"""
from bot import WhatsBot


if __name__ == '__main__':
    # Starting the WhatsBot and authenticating
    bot = WhatsBot(headless=False)
    bot.authenticate()

    # Selecting the contact to talk
    contact = input("Which contact do you want to open? ")

    # Checking if contact exists
    if bot.open_contact(contact):
        # Starts a loop for send messages
        while True:
            message = input("Type your message (Type !quit to exit) ")

            # Finishing the program
            if message == '!quit':
                bot.quit_driver()
                break

            # Send the message
            bot.send_messages(message)
    else:
        print("Contact not found")
