# Telegram ChatGPT Bot

Telegram ChatGPT Bot is an AI-powered language model integrated with the Telegram Bot API. It allows users to have interactive conversations with the bot, ask questions, seek information, or engage in casual conversation.

## Features

- Interactive conversation with an AI-powered language model
- Command-based functionality
- Broadcast messages to all bot users
- Help command with instructions on how to use the bot
- Integration with OpenAI's GPT-3.5 model

## Getting Started

To get started with the Telegram ChatGPT Bot, you can either fork the repository or clone it directly.

### Fork the Repository (For GitHub Users)

1. Click the **Fork** button at the top-right corner of this repository page.
2. After forking, you'll have a copy of the repository in your GitHub account.

### Clone the Repository (For Non-GitHub Users)

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/MznStudios/Telegram-ChatGPT.git
   ```

2. Change into the cloned directory:

   ```bash
   cd Telegram-ChatGPT
   ```

### Set Up Environment Variables

1. Create a copy of the `.env.example` file and name it `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor.

3. Replace `<your_bot_token>` with your Telegram bot token obtained from the BotFather.

4. Replace `<your_api_key>` with your OpenAI GPT-3.5 API key.

## Bot Installation

### Local Deployment

1. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the bot script:

   ```bash
   python bot_script.py
   ```

3. Start a conversation with the bot by sending a message or mentioning it in a Telegram chat.

### Deploy to Heroku

1. Click the **Deploy to Heroku** button below to deploy the bot to Heroku:

   [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MznStudios/Telegram-ChatGPT)

2. On the Heroku deployment page, provide a unique app name and select your region.

3. Set the environment variables on the Heroku app:
   - Set `BOT_TOKEN` as the value for your Telegram bot token obtained from the BotFather.
   - Set `API_KEY` as the value for your OpenAI GPT-3.5 API key.

4. Click the **Deploy app** button to deploy the bot to Heroku.

5. Once the deployment is complete, you can start a conversation with the bot on Telegram.

### Deploy to Replit

1. Click the **Import to Replit** button below to import the bot into Replit:

   [![Run on Replit](https://binbashbanana.github.io/deploy-buttons/buttons/remade/replit.svg)](https://replit.com/github/MznStudios/Telegram-ChatGPT)

2. On the Replit import page, customize the project name if desired and click **Import from GitHub**.

3. Set the environment variables on Replit:
   - Click on the padlock icon in the left sidebar.
   - Add `BOT_TOKEN` as the key and your Telegram bot token obtained from the BotFather as the value.
   - Add `API_KEY` as the key and your OpenAI GPT-3.5 API key as the value.

4. Click the **Run** button to deploy the bot on Replit.

5. Once the deployment is complete, you can start a conversation with the bot on Telegram.

### Deploy to Railway

1. Click the **Deploy to Railway** button below to deploy the bot to Railway:

   [![Deploy on Railway](https://binbashbanana.github.io/deploy-buttons/buttons/remade/railway.svg)](https://railway.app/new/template?template=https://github.com/MznStudios/Telegram-ChatGPT)

2. On the Railway deployment page, authorize the Railway app and select your project.

3. Set the environment variables on the Railway app:
   - Set `BOT_TOKEN` as the value for your Telegram bot token obtained from the BotFather.
   - Set `API_KEY` as the value for your OpenAI GPT-3.5 API key.

4. Click the **Start Deploy** button to deploy the bot to Railway.

5. Once the deployment is complete, you can start a conversation with the bot on Telegram.

### Deploy to Termux

1. Install Termux on your Android device from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/en/packages/com.termux/).

2. Open Termux and run the following command to clone the repository:

   ```bash
   git clone https://github.com/MznStudios/Telegram-ChatGPT.git
   ```

3. Change into the cloned directory:

   ```bash
   cd Telegram-ChatGPT
   ```

4. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

5. Set the environment variables by creating a `.env` file:

   ```bash
   cp .env.example .env
   ```

6. Open the `.env` file and replace `<your_bot_token>` with your Telegram bot token obtained from the BotFather, and `<your_api_key>` with your OpenAI GPT-3.5 API key.

7. Run the bot script:

   ```bash
   python bot_script.py
   ```

8. Start a conversation with the bot by sending a message or mentioning it in a Telegram chat.

### Deploy to VPS

1. Set up a VPS (Virtual Private Server) with your preferred provider. Popular choices include AWS EC2, DigitalOcean, and Linode.

2. Connect to your VPS using SSH.

3. Install Git on the VPS. For example, on Ubuntu, you can use the following command:

   ```bash
   sudo apt update
   sudo apt install git
   ```

4. Clone the repository to the VPS using the following command:

   ```bash
   git clone https://github.com/MznStudios/Telegram-ChatGPT.git
   ```

5. Change into the cloned directory:

   ```bash
   cd Telegram-ChatGPT
   ```

6. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

7. Set the environment variables by creating a `.

env` file:

   ```bash
   cp .env.example .env
   ```

8. Open the `.env` file and replace `<your_bot_token>` with your Telegram bot token obtained from the BotFather, and `<your_api_key>` with your OpenAI GPT-3.5 API key.

9. Run the bot script:

   ```bash
   python bot_script.py
   ```

10. Start a conversation with the bot by sending a message or mentioning it in a Telegram chat.

## Commands

- `/start`: Initiate a conversation with the bot.
- `/help`: Display the help message to get information about using the bot.
- `/broadcast`: Send a broadcast message to all bot users.
- `/gpt <question>`: Ask a question or interact with the ChatGPT model.

## Conversation Guidelines

- The bot has a limited memory and may not remember previous messages or conversations.
- Provide necessary context when referring to something mentioned earlier.
- Feel free to ask questions, seek information, or engage in casual conversation.
- The bot's knowledge is based on data up until September 2021, so recent events may not be known.
- Maintain a polite and respectful tone while interacting with the bot.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Repository Statistics

- Stars: [![GitHub stars](https://img.shields.io/github/stars/MznStudios/Telegram-ChatGPT.svg?style=social&label=Star)](https://github.com/MznStudios/Telegram-ChatGPT)
- Forks: [![GitHub forks](https://img.shields.io/github/forks/MznStudios/Telegram-ChatGPT.svg?style=social&label=Fork)](https://github.com/MznStudios/Telegram-ChatGPT)
- Issues: [![GitHub issues](https://img.shields.io/github/issues/MznStudios/Telegram-ChatGPT.svg)](https://github.com/MznStudios/Telegram-ChatGPT/issues)
- Pull Requests: [![GitHub pull requests](https://img.shields.io/github/issues-pr/MznStudios/Telegram-ChatGPT.svg)](https://github.com/MznStudios/Telegram-ChatGPT/pulls)
- License: [![GitHub license](https://img.shields.io/github/license/MznStudios/Telegram-ChatGPT.svg)](https://github.com/MznStudios/Telegram-ChatGPT/blob/main/LICENSE)
- Last Commit: ![GitHub last commit](https://img.shields.io/github/last-commit/MznStudios/Telegram-ChatGPT.svg)
- Repository Size: ![GitHub repo size](https://img.shields.io/github/repo-size/MznStudios/Telegram-ChatGPT.svg)
- Open Issues: ![GitHub open issues](https://img.shields.io/github/issues-raw/MznStudios/Telegram-ChatGPT.svg)
- Closed Issues: ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/MznStudios/Telegram-ChatGPT.svg)

## License

This project is licensed under the [MIT License](LICENSE).
