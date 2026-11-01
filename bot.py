import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# --- ส่วน Web Server สำหรับ UptimeRobot Ping ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    # รัน Web Server บน พอร์ต 8080
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.start()

# --- ส่วนบอท Discord ---
intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@client.tree.command(name="hello", description="ทักทายกับบอท")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"สวัสดีครับคุณ {interaction.user.mention}!")

if __name__ == "__main__":
    DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    if DISCORD_BOT_TOKEN:
        keep_alive()  # เรียกใช้งาน Web Server ก่อนรันบอท
        client.run(DISCORD_BOT_TOKEN)
