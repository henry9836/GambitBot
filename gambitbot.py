#!/usr/bin/python3
import discord

token = open("token").read()
prefix = '!'

class GambitBot(discord.Client):
    async def processMessage(self, message):
        #Remove Command Prefix
        message.content = message.content[1:]
        if (message.content == "gambify"):
            await message.channel.send("hi :D")


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith(prefix):
            print('Message from {0.author}: {0.content}'.format(message))
            await self.processMessage(message)


def main():
    print(token)
    bot = GambitBot()
    bot.run(token)

if __name__ == "__main__":
    main()