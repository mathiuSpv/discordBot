import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from bot import reload_extensions, sync
from data.roles import isDeveloper

class AdminCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
    def is_owner(interaction: Interaction):
        return isDeveloper(userId= interaction.user.id)
    
    @app_commands.command(name="sync", description="Sincroniza los comandos de barra del bot.")
    @app_commands.check(is_owner)
    async def sync(self, interaction: Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            await reload_extensions(self.bot)
            await sync(self.bot)
            await interaction.followup.send("Comandos de barra sincronizados globalmente.")
        except Exception as e:
            await interaction.followup.send(f"Error al sincronizar los comandos: {e}")
            
    @sync.error
    async def sync_error(self, interaction: Interaction, error):
        if isinstance(error, app_commands.CheckFailure):
            await interaction.response.send_message("No tienes permiso para usar este comando.", ephemeral=True)
    
async def setup(bot: Bot):
    await bot.add_cog(AdminCog(bot))