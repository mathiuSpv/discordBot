from discord import Member, VoiceState
from discord.ext.commands import Cog, Bot
from datetime import datetime, timedelta
from utils.game import GameService

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
                GameService.add_experience(member.id, int(time_diff.total_seconds()))
                
async def setup(bot: Bot):
    await bot.add_cog(TimeTrackerCog(bot))