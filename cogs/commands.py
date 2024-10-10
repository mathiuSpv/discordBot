import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from discord.ext.commands import Bot, Cog;
from discord import app_commands, Interaction;
from data.game import getUserStats, User;

class CommandsCog(Cog):
    def __init__(self, bot : Bot):
        self.bot = bot
    
    @app_commands.command(name = "hello", description = "Saluda al usuario")
    async def hello(self, interaction: Interaction):
        """Comando para saludar al usuario."""
        await interaction.response.send_message(f"¡Hola, puto {interaction.user.mention}!")
    
    @app_commands.command(name="level", description="Tu nivel de experiencia")
    async def level(self, interaction: Interaction):
        user : User = getUserStats(userId= interaction.user.id)
        if(user):
            await interaction.response.send_message(f"{interaction.user.mention} : {user.__dict__} {user.getExperience()}.")

async def setup(bot: Bot):
    await bot.add_cog(CommandsCog(bot))