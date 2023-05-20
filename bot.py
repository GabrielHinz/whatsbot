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
import os
import time
import yaml
import json
from typing import Any

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class WhatsBot:
    def __init__(self, headless=True) -> None:
        """
        Constructor of the WhatsBot class.

        Args:
            headless (bool, optional): Defines whether 
            the webdriver will use the headless option.
        """
        if not os.path.exists(CF['bot']['profile']):
            os.makedirs(CF['bot']['profile'])

        self.driver = opendriver(headless)
        self.driver.get(CF['bot']['url'])
        self.threshold = CF["threshold"]

        time.sleep(self.threshold['page'])

    def quit_driver(self) -> None:
        """
        Stop the running webdriver.

        Returns:
            None
        """
        if self.driver:
            self.driver.quit()

    def find_element(self, element: str) -> Any:
        """
        Finds a web element based on the mapping file.

        Args:
            element (str): Element key to look for in the mapping file.

        Returns:
            Any
        """
        try:
            mp = getmap()
            by, value = (mp[element]["type"], mp[element]["value"])
            elem = self.driver.find_element(by, value)
            return elem
        except:
            return False

    def check_auth(self) -> bool:
        """
        Check if the account is logged in whatsapp.

        Returns:
            bool: True/False
        """
        if self.find_element("logged"):
            return True
        else:
            if self.find_element("home"):
                return False
        raise Exception("Whatsapp Web not found!")
    
    def authenticate(self) -> bool:
        """
        Authenticates the user if he is not logged in.

        Returns:
            bool: True/False
        """
        while not self.check_auth():
            self.driver.quit()
            self.driver = opendriver(False)
            self.driver.get(CF['bot']['url'])
            time.sleep(self.threshold['auth'])
        return True
    
    def open_contact(self, contact: str) -> bool:
        """
        Searches for the contact based on the name and selects the first 
        one found.

        Args:
            contact (str): Registered contact name.

        Returns:
            bool: True/False
        """
        search = self.find_element("search")
        search.click()
        search.send_keys(Keys.CONTROL + "A")
        for letter in contact:
            search.send_keys(letter)
        time.sleep(self.threshold['default'])
        try:
            first_contact = search.find_element(
                "xpath", "//span[@title = '{}']".format(contact)
            )
            first_contact.click()
        except:
            return False
        return True

    def last_message(self) -> str:
        """
        Read the last message sent by any user.

        Returns:
            str: Last message in string format
        """
        last_message = self.find_element("last_message")
        return str(last_message.text) if last_message else ''
    
    def send_messages(self, message: str) -> None:
        """
        Send a message to open chat.

        Args:
            message (str): the content of the message to be sent.

        Returns:
            None
        """
        message_input = self.find_element("message_input")
        message_input.click()

        [ message_input.send_keys(c) for c in ":robot"]
        message_input.send_keys(Keys.ENTER)

        message_title = " *{}* :\n".format(CF['bot']['name'])
        message = message_title + message

        for text in message.split('\n'):
            for letter in text:
                message_input.send_keys(letter)
            message_input.send_keys(Keys.SHIFT + Keys.ENTER)

        message_input.send_keys(Keys.ENTER)


def opendriver(headless: bool=True) -> webdriver:
    """
    Starts a new webdriver for use.

    Args:
        headless (bool, optional): Defines whether the webdriver
        will use the headless option.

    Returns:
        webdriver: The initialized WebDriver object.
    """
    opt = Options()
    opt.add_argument("--profile")
    opt.add_argument(CF['bot']['profile'])

    if headless and CF['bot']['headless']:
        opt.add_argument("--headless")

    driver = webdriver.Firefox(
        options=opt, service_args=["--marionette-port", CF['bot']['marionette']]
    )
    return driver


def config() -> yaml:
    """
    Loads and returns the YAML configuration file.

    Returns:
        yaml: The parsed YAML configuration object.
    """
    with open('config.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config


def getmap() -> json:
    """
    Loads and returns the JSON mapping file.

    Returns:
        yaml: The parsed JSON mapping object.
    """
    filename = CF["map"]["file"]
    with open(filename, 'r') as config_file:
        mapping = json.load(config_file)
    return mapping


# Initialize the constants
CF = config()
