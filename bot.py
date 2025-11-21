import os
import discord
from discord.ext import commands
from ai import consultar_ia
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot iniciado como {bot.user}")

@bot.command()
async def ask(ctx, *, pregunta):
    await ctx.send("Pensando... 🤖💭")

    respuesta = consultar_ia(pregunta)

    # Discord limita mensajes a 2000 caracteres
    if len(respuesta) > 2000:
        respuesta = respuesta[:1990] + "..."

    await ctx.send(respuesta)

bot.run(TOKEN)
