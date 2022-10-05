import discord
from discord.ext import commands
from myserver import server_on

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        if message.content.startswith('help?'):
            embedVar = discord.Embed(title="Command", description="LIST OF COMMANDS", color=0x00ff00)
            embedVar.add_field(name="who?", value="Type who?", inline=False)
            embedVar.add_field(name="Programming command", value="Type Programming? to see detail", inline=False)
            embedVar.add_field(name="Hololive?", value="Type Hololive? to see detail", inline=False)
            await message.channel.send(embed=embedVar)

        if message.content == 'who?':
            await message.channel.send('https://www.maikelfapk.site/')

        if message.content == 'HTML?':
            await message.channel.send('https://www.w3schools.com/html/default.asp')

        if message.content == 'CSS?':
            await message.channel.send('https://www.w3schools.com/css/default.asp')

        if message.content == 'JS?':
            await message.channel.send('https://www.w3schools.com/js/default.asp')

        if message.content.startswith('Hololive?'):
            embedVar = discord.Embed(title="Search?", description="Result", color=0x00ff00)
            embedVar.add_field(name="Hololive EN", value="https://www.maikelfapk.site/html/hololiveen", inline=False)
            embedVar.add_field(name="Hololive JP", value="https://www.maikelfapk.site/html/hololivejp", inline=False)
            embedVar.add_field(name="Hololive ID", value="https://www.maikelfapk.site/html/hololiveid", inline=False)
            await message.channel.send(embed=embedVar)

        if message.content.startswith('Programming'):
            embedVar = discord.Embed(title="Command", description="LIST OF PROGRAMMING COMMANDS", color=0x00ff00)
            embedVar.add_field(name="HTML?", value="For HTML", inline=False)
            embedVar.add_field(name="CSS?", value="For CSS", inline=False)
            embedVar.add_field(name="JS?", value="For JavaScript", inline=False)
            await message.channel.send(embed=embedVar)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run('Your Token')