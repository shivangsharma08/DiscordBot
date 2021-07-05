import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")

# Code to check is bot is ready or not


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching Your Server'))
    print("Bot is ready")

# Code to respond to Greetings


@client.command(aliases=['hi', 'hey'])
async def hello(ctx):
    await ctx.send("Hey there!")

# Code for about


@client.command()
async def about(ctx):
    await ctx.send("Hi there! My name is Shivang. I am from New Delhi, India. I develop web applications and produce fire ass beats 🔥🎵")

# Code to get the list of games


@client.command()
async def games(ctx):

    f = open("games.txt", "r")
    gms = f.read()
    await ctx.send(gms)

# Code for rock, paper and scissors game


@client.command(aliases=['rockpaperscissors', 'rockpaperscissor'])
async def rps(ctx, *, chc):
    responses = ['rock',
                 'paper',
                 'scissors']
    bres = random.choice(responses)
    await ctx.send(f'You picked: {chc}\nBot picked: {bres}')
    if(chc == 'paper' and bres == 'rock'):
        await ctx.send('You won!')
    elif(chc == 'paper' and bres == 'scissors'):
        await ctx.send('Bot won!')
    elif(chc == 'paper' and bres == 'paper'):
        await ctx.send("It's a tie!")
    elif(chc == 'rock' and bres == 'paper'):
        await ctx.send("Bot won!")
    elif(chc == 'rock' and bres == 'scissors'):
        await ctx.send('You won!')
    elif(chc == 'rock' and bres == 'rock'):
        await ctx.send("It's a tie!")
    elif(chc == 'scissors' and bres == 'paper'):
        await ctx.send('You won!')
    elif(chc == 'scissors' and bres == 'rock'):
        await ctx.send('Bot won!')
    elif(chc == 'scissors' and bres == 'scissors'):
        await ctx.send("It's a tie!")
    else:
        await ctx.send("Please enter a valid choice.")

# Code for bye


@client.command(aliases=['goodbye'])
async def bye(ctx):
    responses = ['See you later!',      
                 'Bye, take care!',
                 ]
    await ctx.send(random.choice(responses))

# Code to clear messages


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

client.run('Your discord token')
