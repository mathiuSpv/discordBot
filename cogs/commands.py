from discord.ext.commands import Bot, Cog;
from discord import app_commands, Interaction;
from utils.game import UserGameDTO, GameService;

class CommandsCog(Cog):
    def __init__(self, bot : Bot):
        self.bot = bot
    
    @app_commands.command(name="level", description="Tu nivel de experiencia")
    async def level(self, interaction: Interaction):
        response : UserGameDTO = GameService.get_user(interaction.user.id)
        if(response):
            await interaction.response.send_message(
                f"""{interaction.user.mention} : {response.lvl} ({response.exp}/ {response.end}).""")

async def setup(bot: Bot):
    await bot.add_cog(CommandsCog(bot))