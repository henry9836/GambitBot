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
        args = messageContent.split(' ')

        #Gambify Command
        if (args[0] == "gambify"):
            searchTemp = gambitSearchHistroy
            if (len(args) > 1):
                try:
                    searchTemp = int(args[1])
                except:
                    print(args[1] + " is not a valid argument")
            messages = await messageChannel.history(limit=searchTemp).flatten()
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
                            #If is cris
                            if (str(messages[i].author.id) == "205899903594004489"):
                                await messages[i].delete()
                            await messageChannel.send(response)
                            return
            await message.reply("Could not find a message long enough to grace with gambit >w<")
        elif (args[0] == "update"):
            #Volt or Nitro
            if (message.author.id == "102606498860896256") or (message.author.id == "269672239245295617"):
                print("Updating...")
                exit(0)
        return

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith(prefix):
            await self.processMessage(message)


def main():
    bot = GambitBot()
    bot.run(token)

if __name__ == "__main__":
    main()