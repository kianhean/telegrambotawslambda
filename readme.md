
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

### Setup Your Project Variables

Open zappa_settings.json and replace <YOURNAME> with the name of your project


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

The reply returned should be True.

Speak to your bot!


### Updating your bot

Updates to your bot can be done and then sent to production using

```bash
zappa update
```