from discord.ext.commands import Bot, Cog;
from discord import app_commands, Interaction;

class NotificadorCog(Cog):
    def __init__(self, bot : Bot):
        self.bot = bot

async def setup(bot: Bot):
    await bot.add_cog(NotificadorCog(bot))