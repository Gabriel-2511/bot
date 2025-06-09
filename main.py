import discord
from discord.ext import commands
from bot_logic import gen_pass

#Programa en donde aprendimos a usar la clase Bot.

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como', bot.user)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot, {bot.user}!')

@bot.command()
async def color(ctx):
    await ctx.send('Mi color favorito es el azul')

@bot.command()
async def passw(ctx):
    await ctx.send ("Contraseña:" + gen_pass(10))
    
bot.run("Token")
