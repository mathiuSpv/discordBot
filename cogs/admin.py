from discord import app_commands, Interaction
from discord.ext.commands import Bot, Cog
from bot import reload_extensions, sync

class AdminCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @app_commands.command(name="sync", description="Sincroniza los comandos de barra del bot.")
    @app_commands.check(1==1)
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