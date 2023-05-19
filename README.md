# WhatsApp Bot

This project implements a WhatsApp bot using the Selenium WebDriver. The bot is designed to automate various interactions on the WhatsApp platform, such as authenticating, opening contacts, reading messages, and sending messages.

## Requirements

Before running the project, make sure you have the following requirements installed:

- Python (version 3.8.7)

## Installation

1. Clone the repository:

  ```shell
  git clone https://github.com/GabrielHinz/whatsbot.git 
  ```
   
2. Navigate to the project directory:

  ```shell
  cd whatsbot
  ```

3. Installing dependencies:

  ```shell
  pip install -r requirements.txt
  ``` 
   
## Configuration
 Change the configuration in the config.yml file.

## Example Usage
1. Run the `example.py` file:
  
  ```shell
  python example.py
  ```
  **Note:** The first time you run this program it will authenticate in whatsapp, if it takes too long it may timeout. Adjust the time in the config file if needed.
  
## Contribution
If you would like to contribute to this project, please follow the steps below:

1. Fork this repository.
2. Create a feature branch (git checkout -b feature/feature-name).
3. Make the desired changes.
4. Commit the changes (git commit -am 'Add a new feature').
5. Push to the branch (git push origin feature/feature-name).
6. Open a Pull Request.

## Authors
- **Gabriel Hinz** - *DevOps Eng.* -
    [About](https://gabriel.legendproject.com.br/)
    
## License
This project is licensed under the MIT License (LICENSE.md)