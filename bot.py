import os, asyncio;
from discord import Intents;
from discord.ext.commands import Bot;
from dotenv import load_dotenv;
from utils.printer import status_message
from discord.ext.commands.errors import ExtensionFailed, ExtensionAlreadyLoaded, ExtensionNotLoaded;

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPLICATION_ID = os.getenv('DISCORD_APLICATION_ID')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

#PRIVATE CHANNEL
_intents : Intents = Intents.default()
_intents.message_content = True
_intents.members = True
_intents.presences = True

_bot = Bot(command_prefix=">", intents=_intents, application_id=APPLICATION_ID)

@_bot.event
async def on_ready():
    try:
        await sync(bot= _bot)
    except Exception as e:
        status_message("error", f"Error al sincronizar los comandos de barra: \n    {e}")
    status_message("finalizado",  "El bot ha iniciado con éxito")
    return


async def _load_extensions_(bot : Bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                cog = filename[:-3]
                status_message("ejecucion", f"Extension cogs.{cog} ejecutandoce.")
                await bot.load_extension(f'cogs.{cog}')
            except ExtensionAlreadyLoaded:
                pass
            except ExtensionFailed:
                status_message("error", f"Extension cogs.{cog} no se pudo cargar")
            except Exception as e:
                status_message("error", f"Extension cogs.{cog} no se pudo cargar: \n {e}")
    status_message("finalizado", "Cogs cargados.")
    return

async def _unload_extensions_(bot : Bot):
    extensions = len(bot.extensions)
    if(extensions != 0):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    cog = filename[:-3]
                    await bot.unload_extension(f'cogs.{cog}')
                    status_message("aviso", f"Extension cogs.{cog} desactivada.")
                except ExtensionNotLoaded:
                    status_message("error", f"Extension cogs.{cog} no se encontraba activa")
                except Exception as e:
                    status_message("error", f"Extension cogs.{cog} no se pudo desactivar: \n{e}")
        status_message("finalizado", "Cogs desactivados.")
    return
                
async def sync(bot : Bot):
    await bot.tree.sync()
    status_message("finalizado", "Comandos de barra sincronizados exitosamente.")
    return
                
async def reload_extensions(bot: Bot):
    await _unload_extensions_(bot)
    await _load_extensions_(bot)
    return
    
async def _main_(bot : Bot):
    async with bot:
        await _load_extensions_(bot)
        await bot.start(TOKEN)
    return

if __name__ == "__main__":
    asyncio.run(_main_(_bot))