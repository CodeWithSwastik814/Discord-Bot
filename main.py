import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
SECRET_ROLE = "CODER"

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"All preparations complete. We enter and take what's ours {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Here you are, {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower() or "damn" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Watch your Language Mortal.")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Long Time no see, {ctx.author.mention}!")
    
@bot.command()
async def coder(ctx):
    role = discord.utils.get(ctx.guild.roles, name=SECRET_ROLE)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, You are assigned to be a {SECRET_ROLE}")
    else:
        await ctx.send("Not Worthy")
        
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("😀")
    await poll_message.add_reaction("😡")
        
bot.run(token, log_handler=handler, log_level=logging.DEBUG)