import os
import discord
from discord import app_commands
from discord.ext import commands

# ตั้งค่า Intents สำหรับบอท
intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    try:
        # ซิงค์ Slash Commands เข้ากับ Discord
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# ตัวอย่างคำสั่ง Slash Command (/hello)
@client.tree.command(name="hello", description="ทักทายกับบอท Roblox ของคุณ")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"สวัสดีครับคุณ {interaction.user.mention}! บอทพร้อมรับคำสั่งแล้วครับ 🚀")

# ดึง Token จาก Environment Variables
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

if __name__ == "__main__":
    if not DISCORD_BOT_TOKEN:
        print("Error: ไม่พบ DISCORD_BOT_TOKEN ใน Environment Variables")
    else:
        client.run(DISCORD_BOT_TOKEN)
