import discord
from discord.ext import commands
from book_recommender import generate_book_recommendation

BOT_TOKEN = 'MTE4ODM5MDk3OTgyOTUxMDE2NA.Gkeben.Te_BxWaA5IZwkPJ8PivPSn_gP4Uz5o-QAiQKqY'
CHANNEL_ID = 1188393262298439720

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("hi! book recommender bot is ready! :)")
    # channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("hi! :)")

@bot.command()
async def recommend(ctx, genre):
    genre = str(genre)
    result = generate_book_recommendation(genre)
    await ctx.send(f"{result}")
bot.run(BOT_TOKEN)
