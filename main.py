
from telethon import TelegramClient, events
from Config import API_ID, API_HASH, BOT_TOKEN, SOURCE_CHANNELS, DESTINATION_CHANNEL

client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        await event.forward_to(DESTINATION_CHANNEL)
        print(f"✅ Forwarded message from {event.chat.username}")
    except Exception as e:
        print("❌ Error:", e)

print("🚀 Bot starting...")
client.start(bot_token=BOT_TOKEN)
print("🤖 Bot is running and listening for messages...")
client.run_until_disconnected()
