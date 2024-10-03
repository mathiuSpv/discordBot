from discord.ext import commands;
from discord.ext.commands import Bot, Cog;

class HiCog(Cog):
    def __init__(self, bot : Bot):
        self.bot = bot
    
    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send('¡Hola! Soy un comando dentro del Cog Test.')

    @commands.command(name='bye')
    async def bye(self, ctx):
        await ctx.send('¡Adiós! Este es otro comando de prueba.')
        
async def setup(bot : Bot):
    await bot.add_cog(HiCog(bot))

if __name__ == "__main__":
    import asyncio, os, sys;
    
    # add local path to sys.path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

    # import cog_start
    from bot import cog_start;
    asyncio.run(cog_start("hi"))