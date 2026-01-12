import discord
from discord import app_commands
import os

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

CANAL_PERMITIDO_ID = 123456789012345678  # troque pelo ID do canal

@client.event
async def on_ready():
    await tree.sync()
    print(f"🤖 Bot conectado como {client.user}")

# 🔹 /build
@tree.command(name="build", description="Cria uma thread privada para montar sua build")
async def build(interaction: discord.Interaction):

    # ❌ Bloquear uso dentro de thread
    if isinstance(interaction.channel, discord.Thread):
        await interaction.response.send_message(
            "❌ Use este comando no canal principal.",
            ephemeral=True
        )
        return

    # ❌ Bloquear canal errado
    if interaction.channel.id != CANAL_PERMITIDO_ID:
        await interaction.response.send_message(
            "❌ Use este comando no canal correto.",
            ephemeral=True
        )
        return

    # ✅ Criar thread privada
    thread = await interaction.channel.create_thread(
        name=f"⚽ Build - {interaction.user.name}",
        type=discord.ChannelType.private_thread,
        invitable=False
    )

    await thread.add_user(interaction.user)

    await interaction.response.send_message(
        "✅ Thread criada! Confira acima 👆",
        ephemeral=True
    )

    await thread.send(
        f"👋 Olá {interaction.user.mention}!\nVamos montar sua build passo a passo."
    )

client.run(os.getenv("DISCORD_TOKEN"))
