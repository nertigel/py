# py

### tg_announce_subs_bot
This script will log a users' ID & language and save it to a file named `users.txt` after they start the bot(`/start`), an array named `allowed_users` contains IDs of users who can use the `/announce` command, 
the `/announce` command will take an argument and iterate through the `users.txt` file and lastly it will send a message to all users that were in the file.
