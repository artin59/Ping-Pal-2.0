import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.dm_messages = True
intents.emojis = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='baller', intents=intents)

@bot.command()
async def dm(ctx, role:discord.Role, *, message):

    message = message + '\n' + "From: " + str(ctx.guild) + '\n' + "By: " + str(ctx.author)
    embed = discord.Embed(title=message)

    for member in role.members:
        await member.send(embed=embed)

    await ctx.channel.send('DMs Sent Successfully')


@bot.command()
async def dmuser(ctx, user:discord.Member, *, message):

    message = message + '\n' + "From: " + str(ctx.guild) + '\n' + "By: " + str(ctx.author)
    embed = discord.Embed(title=message)

    await user.send(embed=embed)
    await ctx.channel.send('DM Sent Successfully')

@bot.command()
async def assign(ctx, *, role:discord.Role):

    for member in ctx.channel.members:
        await member.add_roles(role)

    await ctx.channel.send('All Roles Assigned Successfully')



bot.run(token, log_handler=handler, log_level=logging.DEBUG)