# Votekick
 Allow chatters to collectively kick mischievous people in your Discord server!

## Commands
### `!votekick <user> <reason>`
#### Aliases: `!vk`
Starts a vote to kick someone for a reason.

### `!vote_requirement`
#### Default: `3`
Changes the requirement amount of votes to kick someone.

## Setup
Install dependencies with
```shell
pip install -r requirements.txt
```
make sure your token is set in `.env`
```ini
TOKEN="BlahBlahBlah"
```
and run with
```shell
python main.py
```