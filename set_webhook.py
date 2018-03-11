#!/usr/bin/python

bot_token = <your telegram token here>

import telepot
bot = telepot.Bot(bot_token)

#Set AWS endpoint gateway
bot.setWebhook("https://XXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev")

#terminate webhook if sth gets wrong
#bot.setWebhook("")

print(bot.getMe())
