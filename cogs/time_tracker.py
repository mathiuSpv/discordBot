import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from discord import Member, VoiceState
from discord.ext.commands import Cog, Bot
from datetime import datetime, timedelta
import data.sql_function as sql

class TimeTrackerCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.user_entry_time = dict()
        
    @Cog.listener()
    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState):
        if before.channel is None and after.channel is not None:
            self.user_entry_time[member.id] = datetime.now()

        elif before.channel is not None and after.channel is None:
            if member.id in self.user_entry_time:
                entry_time = self.user_entry_time.pop(member.id)
                exit_time = datetime.now()
                time_diff : timedelta = (exit_time  - entry_time)
                second_experience : int = int(time_diff.total_seconds())
                exist, _ = sql.getUser(member.id)
                if (exist):
                    sql.updateUserExp(member.id, second_experience)
                else:
                    sql.insertUser(member.id, second_experience)
                
    
async def setup(bot: Bot):
    await bot.add_cog(TimeTrackerCog(bot))

if __name__ == "__main__":
    import asyncio, os, sys

    # Importar la función cog_start desde el archivo principal
    from bot import cog_start
    asyncio.run(cog_start("time_tracker"))