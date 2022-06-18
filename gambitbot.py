#!/usr/bin/python3
import discord

token = open("token").read()
prefix = '!'
gambitReplaceNthWord = 4
gambitSearchHistroy = 3

class GambitBot(discord.Client):

    async def processMessage(self, message):
        #Remove Command Prefix
        messageContent = message.content[1:]
        messageChannel = message.channel

        #Gambify Command
        if (messageContent == "gambify"):
            messages = await messageChannel.history(limit=gambitSearchHistroy).flatten()
            for i in range(len(messages)):
                if i != 0:
                    if (messages[i].author != self.user):
                        responseList = messages[i].content.split(' ')
                        if (len(responseList) >= 4):
                            #Replace every nth word with gambit
                            for x in range(len(responseList)):
                                if (x % gambitReplaceNthWord) == 0 and x != 0:
                                    responseList[x] = "gambit"
                            response = '"' + ' '.join(responseList) + '" - <@' + str(messages[i].author.id) + '>'
                            await messageChannel.send(response)
                            return
        await message.reply("Could not find a message long enough to grace with gambit >w<")
        return

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

if __name__ == "__main__":
    main()