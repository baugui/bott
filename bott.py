import discord
from discord.ext import commands
from IA import get_class
import os
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
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            nombre = attachment.filename
            direccion = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image_path=f'./{attachment.filename}',model_path='./keras.model.h5' ), labels_path='./labels.txt')
    else:
        await ctx.send("No funciona")
        
    
        

bot.run("MTIxNzUyMTgyNzE4NzAwMzQyMw.GmfV5C.5l93OIzde4h1BXtr5n7GJtk7XQgQT_TrQcU0zk")