from telethon import TelegramClient, events
from config import API_ID, API_HASH, SOURCE_CHANNELS, TARGET_CHANNEL

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
    except Exception as e:
        print("Error:", e)

print("Bot running...")
client.start()
client.run_until_disconnected()
