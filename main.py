import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def build(ctx):
    if isinstance(ctx.channel, discord.Thread):
        await ctx.send("❌ Use este comando no canal principal.")
        return

    thread = await ctx.channel.create_thread(
        name=f"Build • {ctx.author.name}",
        type=discord.ChannelType.private_thread
    )

    await thread.add_user(ctx.author)

    await thread.send(
        f"👋 Olá {ctx.author.mention}!\n\n"
        "Essa conversa é **privada**.\n"
        "Vou te ajudar a montar sua build do **TOUCHLINE ⚽**\n\n"
        "👉 Primeiro: você joga **PC ou Mobile**?"
    )

bot.run(os.getenv("DISCORD_TOKEN"))
