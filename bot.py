import os, asyncio;
from discord import Intents;
from discord.ext.commands import Bot;
from dotenv import load_dotenv;

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

#PRIVATE CHANNEL
__intents : Intents = Intents.default()
__intents.message_content = True
__intents.members = True
__intents.presences = True

bot : Bot = Bot(command_prefix=">", intents=__intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
  
async def cog_start(name: str):
    async with bot:
        await bot.load_extension(f"cogs.{name}")
        await bot.start(TOKEN)  
    
async def __load_cogs__():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def __main__():
    async with bot:
        await __load_cogs__()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(__main__())