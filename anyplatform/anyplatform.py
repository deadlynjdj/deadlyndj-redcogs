import discord
from redbot.core import commands


class AnyPlatform(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, message):
        if not isinstance(message.channel, discord.TextChannel):
            return

        if message.type != discord.MessageType.default:
            return

        if message.author.id == self.bot.user.id:
            return

        if message.author.bot:
            return

        content = message.clean_content
        if len(content) == 0:
            return
        if content.lower().startswith("https://open.spotify.com/track/") and not (':' in content) and \
                        len(content) < 50:
            try:
                message = content
                await message.channel.send("Hi, {message}".format(message=message),
                               allowed_mentions=discord.AllowedMentions(
                               everyone=False, roles=False, users=False))
            except (discord.HTTPException, discord.Forbidden, ):
                pass
