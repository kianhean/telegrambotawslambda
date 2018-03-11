
# Telegram Bot Lambda Boilerplate using Zappa + Hug + Telepot

### Git Clone this repo

```bash
git clone https://github.com/kianhean/telegrambotawslambda.git
```

### Initial setup

```bash
pipenv --three
pipenv install
```

### Make sure you have installed Zappa and awscli in your project directory
```bash
pipenv install awscli
pipenv install zappa
```

### Setup Your Project Variables

Open zappa_settings.json and replace <YOURNAME> with the name of your project

### create a AWS IAM role for zappa
(please refer to reference)

### Setup Your Telegram Bot's Key

If you dont have one please go to @botfather to get one

Open app.py and replace <TELEGRAMAPIKEY> with your key from botfather


### Deploy on AWS Lambda

Assuming you have sufficient permissions run the following commands in the shell

```bash
pipenv shell
zappa deploy
```

Take note of the endpoint of your bot. Will look similar to the following

```bash
https://xxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev
```

### Telling Telegram your Bot is alive

Send the following curl to Telegram to inform them of your endpoint. Replace the variables below with your own

```bash
curl --data "url=<YOUR URL ABOVE>" "https://api.telegram.org/bot<TELEGRAMAPIKEY>/setWebhook"
```
(I prefer to use a python script to do so instead. Please refer to set_webhook.py)

The reply returned should be True.

Speak to your bot!


### Updating your bot

Updates to your bot can be done and then sent to production using

```bash
zappa update
```

### Tips
1. ngrok (https://ngrok.com/) is a very good way to test your code before deploying to AWS lambda. Please refer to item 1 of the reference for details.

### Some useful reference
1.  https://medium.freecodecamp.org/how-to-build-a-server-less-telegram-bot-227f842f4706
2.  https://taiosolve.xyz/first-steps-with-aws-lambda-zappa-flask-and-python-3/
3. https://www.viget.com/articles/building-a-simple-api-with-amazon-lambda-and-zappa/
