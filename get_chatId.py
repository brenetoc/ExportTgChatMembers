import os
import asyncio

from dotenv import load_dotenv
from telethon import TelegramClient


load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHAT_NAME = os.getenv("CHAT_NAME")


async def main():
    async with TelegramClient(
        "telegram_session",
        API_ID,
        API_HASH
    ) as client:

        print(f"Ищу группу: {CHAT_NAME}")
        print()

        async for dialog in client.iter_dialogs():
            if dialog.name == CHAT_NAME:
                print("✅ Группа найдена!")
                print(f"Название: {dialog.name}")
                print(f"ID: {dialog.id}")
                return

        print("❌ Группа с таким названием не найдена.")


if __name__ == "__main__":
    asyncio.run(main())
