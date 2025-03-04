from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="create_voice")
    async def create_voice_channel(self, ctx, channel_name: str):
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name="🎙️ VOICE-CHANNELS")
        
        if not category:
            category = await guild.create_category("🎙️ VOICE-CHANNELS")

        channel = await guild.create_voice_channel(channel_name, category=category)
        await ctx.send(f'✅ Sprachkanal **{channel.name}** wurde erstellt.')

    @commands.command(name="delete_voice")
    async def delete_voice_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
        if channel:
            await channel.delete()
            await ctx.send(f'❌ Sprachkanal **{channel_name}** wurde gelöscht.')
        else:
            await ctx.send(f'⚠️ Kein Sprachkanal mit dem Namen **{channel_name}** gefunden.')

def setup(bot):
    bot.add_cog(Voice(bot))
