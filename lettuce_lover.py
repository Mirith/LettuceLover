import discord
import argparse
from pathlib import Path

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello bot'):
        await message.channel.send("OH HI")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='start bot "safely"')
    parser.add_argument("-s", "--secret", help='file location with secret')

    args = parser.parse_args()

    secret = Path(args.secret).read_text()

    client.run(secret)
    on_message()