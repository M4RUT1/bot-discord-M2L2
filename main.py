import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10')

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    with open('images/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def answer(ctx, n):
    if n == random.randint(1, 10):
        await ctx.send('Congrats, You guessed the right number!')
    else:
        await ctx.send('Skill Issue')

@bot.command()
async def trash(ctx):
    await ctx.send('What Classification of Trash do u want to know? Answer with garbage')

@bot.command()
async def garbage(ctx, f):
    if f == "organic":
        await ctx.send('green waste, food waste, food-soiled paper, non-hazardous wood waste, green waste, and landscape and pruning waste.')
    elif f == "inorganic":
        await ctx.send('plastic soda bottles, glass, yogurt cups, spoons, cellophane, aluminum cans, plastic bags.')
    elif f == "B3":
        await ctx.send('used lubricants, used batteries, used filters, B3 contaminated materials, and medical waste')



bot.run("")
