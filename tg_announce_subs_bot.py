# explanation: everytime a user starts a conversation with the bot, their ID will be stored.
# then you have the option to use the /announce command with a message to all users IDs that were stored in the file.
# this can be used if your group/channel has been deleted and you would like to send a new link to old members.

from telegram import Bot
from telegram.ext import CommandHandler, Application

allowed_users = [2561194827, 654984951111] # user ids
bot_token = "123:abc"
bot = Bot(bot_token)

with open('users.txt', 'a') as file:
    print("users.txt exists")

async def start(update, context):
    user = update.message.from_user

    # make sure we aint got duplicates
    with open('users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            ex_user_id = line.split(',')[0]
            if ex_user_id == str(user.id):
                print(f"{ex_user_id} already exists in our db")
                return

    with open('users.txt', 'a') as file:
        file.write(f'{user.id},{user.language_code}\n')
    print(f"added {user.id} to db")
    #update.message.reply_text('you have been added to the database')

async def announce(update, context):
    if update.effective_user.id in allowed_users:
        args = context.args
        if len(args) == 0:
            return
        message = ' '.join(args)

        with open('users.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            user_id, language = line.strip().split(',')
            await bot.send_message(chat_id=user_id, text=message)
            print(f"sent message to {user_id}")

def main() -> None:
    application = Application.builder().token(bot_token).build()

    __handlers__ = {}
    __handlers__["start_cmd"] = CommandHandler("start", start)
    __handlers__["announce"] = CommandHandler("announce", announce)

    for name, handler in __handlers__.items():
        application.add_handler(handler)
        print(f'Added handler {name}')

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()