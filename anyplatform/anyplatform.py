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
            # this is a bot, discard early
            return

        content = message.clean_content
        if len(content) == 0:
            # nothing to do, exit early
            return
        if content.lower().startswith("https://open.spotify.com/track/") or ("https://music.apple.com/"):
            try:
                url = content
                await message.channel.send("https://song.link/{url}".format(url=url),
                               allowed_mentions=discord.AllowedMentions(
                               everyone=False, roles=False, users=False))
            except (discord.HTTPException, discord.Forbidden, ):
                pass