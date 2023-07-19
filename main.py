import os
import logging
import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Load the environment variables from .env.example
load_dotenv('.env.example')

# Get the token from the environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')

if BOT_TOKEN is None:
    logging.error("Telegram bot token not found in the environment variables. Please provide the token in the .env.example file.")
    exit()

if API_KEY is None:
    logging.error("API key not found in the environment variables. Please provide the key in the .env.example file.")
    exit()

# Define a function to handle the /start command
def start_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://telegra.ph/file/your_image.jpg',
                           caption=f"👋 Hello {user.first_name}, Welcome to Telegram ChatGPT Bot! 🤖💬\n\n"
                                   "I'm an AI-powered language model here to assist and chat with you. "
                                   "Whether you have questions, need help, or just want to have a friendly "
                                   "conversation, I'm here for you! 🎉\n\n"
                                   "Feel free to ask me anything, share your thoughts, or discuss various "
                                   "topics. I'm equipped with knowledge up until September 2021, so keep that "
                                   "in mind when asking about recent events.\n\n"
                                   "Let's get started and have some fun together! 😄✨",
                           reply_markup=InlineKeyboardMarkup([
                               [InlineKeyboardButton('🧑‍💻 Follow Developer on Github', url='https://github.com/MznStudios')],
                               [InlineKeyboardButton('🌐 Bot Script', url='https://github.com/MznStudios/bot-script')]
                           ]))

# Define a function to handle the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    user_id = str(update.effective_user.id)
    if user_id == "122453849":
        help_text = "🤖 Welcome to Telegram ChatGPT Bot Help! 🚀\n\n" \
                    "I'm here to assist you in using Maazin's Telegram ChatGPT Bot and make your chatbot experience enjoyable. Here are some instructions to get you started:\n\n" \
                    "1️⃣ Invoking the Bot:\n" \
                    "To start interacting with the bot, simply mention or send a message to @MZN_ChatGPTBot in your Telegram chat.\n\n" \
                    "2️⃣ Conversation:\n" \
                    "Type your message or question after invoking the bot, and it will respond accordingly. You can have a back-and-forth conversation with the bot, just like chatting with a friend.\n\n" \
                    "3️⃣ Command List:\n" \
                    "You can use the following commands to interact with the bot:\n\n" \
                    "- /help: Display the help message to get information about using the bot.\n" \
                    "- /start: Initiate a conversation with the bot.\n" \
                    "- /broadcast: Send a broadcast message to all bot users.\n" \
                    "- /gpt: Ask a question or interact with the ChatGPT model.\n\n" \
                    "4️⃣ Context and Memory:\n" \
                    "The bot has a limited memory and may not remember previous messages or conversations. If you refer to something mentioned earlier, please provide necessary context to help the bot understand your query.\n\n" \
                    "5️⃣ Natural Language Queries:\n" \
                    "Feel free to ask questions, seek information, or engage in casual conversation. The bot is trained on a wide range of topics but has a knowledge cutoff in September 2021. It may not be aware of recent events or updates.\n\n" \
                    "6️⃣ Politeness and Respect:\n" \
                    "Please maintain a polite and respectful tone while interacting with the bot. The bot is designed to assist and provide helpful responses, but it's important to remember that it is an AI and may not fully understand complex or sensitive queries.\n\n" \
                    "If you encounter any issues or have feedback, feel free to contact Maazin, the developer of this bot. Enjoy your conversation with Telegram ChatGPT Bot! 🎉🤗"
    else:
        help_text = "You are not authorized to access the help command."
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

# Define a function to handle the /broadcast command
def broadcast_command(update: Update, context: CallbackContext) -> None:
    user_id = str(update.effective_user.id)
    if user_id == "122453849":
        text = update.message.reply_to_message.text
        all_users = context.bot.get_chat_members_count(update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Broadcasting to {all_users} users:\n\n{text}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, you are not authorized to use the broadcast command.")

# Define a function to handle user messages
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text.lower() == "reset":
        # Clear the conversation history
        context.user_data.clear()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Conversation has been reset. You can start a new conversation.")
    elif text.lower().startswith("gpt"):
        question = text[4:].strip()
        if question:
            # Make a request to the ChatGPT API
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "system", "content": "You are a helpful assistant."},
                                 {"role": "user", "content": question}]
                }
            )

            # Process the API response and retrieve the model's reply
            if response.status_code == 200:
                data = response.json()
                model_reply = data["choices"][0]["message"]["content"]
                context.bot.send_message(chat_id=update.effective_chat.id, text=model_reply)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I couldn't get a response from ChatGPT at the moment.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a question after the 'gpt' command.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='You said: ' + text)

def main() -> None:
    # Create the bot object
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    start_handler = CommandHandler('start', start_command)
    help_handler = CommandHandler('help', help_command)
    broadcast_handler = CommandHandler('broadcast', broadcast_command)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(broadcast_handler)

    # Register message handler
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    logging.info("Bot started.")

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
