from discord.ext.commands import Bot, Cog
from discord import app_commands, Interaction

class HiCog(Cog):
    def __init__(self, bot : Bot):
        self.bot = bot
    
    @app_commands.command(name = "hello", description = "Saluda al usuario")
    async def hello(self, interaction: Interaction):
        """Comando para saludar al usuario."""
        await interaction.response.send_message(f"¡Hola, {interaction.user.mention}!")

async def setup(bot: Bot):
    await bot.add_cog(HiCog(bot))

if __name__ == "__main__":
    import asyncio, os, sys

    # Añadir la ruta principal al sys.path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

    # Importar la función cog_start desde el archivo principal
    from bot import cog_start
    asyncio.run(cog_start("hi"))