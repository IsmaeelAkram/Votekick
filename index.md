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
### With Docker
The easiest way to get started is using Docker. Build the docker image using:
```shell
docker build -t votekick-bot .
```
and run it using:
```shell
docker run -it --rm votekick-bot
```

### Without Docker
Install dependencies with:
```shell
pip install -r requirements.txt
```
make sure your token is set in `.env` like this:
```ini
TOKEN="BlahBlahBlah"
```
and run the program with:
```shell
python main.py
```
