import os
import csv
import asyncio

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import User

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

CHAT_ID = int(os.getenv("CHAT_ID"))
CHAT_NAME = os.getenv("CHAT_NAME")

# =========================

async def main():
    client = TelegramClient(
        "telegram_session",
        API_ID,
        API_HASH
    )

    await client.start()

    print("Подключено.")
    print(f"Получаю участников: {CHAT_NAME}")
    print(f"ID: {CHAT_ID}")

    entity = await client.get_entity(CHAT_ID)

    members = []

    async for user in client.iter_participants(entity):
        if not isinstance(user, User):
            continue

        username = user.username or ""

        members.append({
            "id": user.id,
            "username": username,
            "first_name": user.first_name or "",
            "last_name": user.last_name or "",
        })

    print(f"Всего участников получено: {len(members)}")

    # =========================
    # usernames.txt
    # =========================

    usernames = sorted(
        {
            "@" + member["username"]
            for member in members
            if member["username"]
        },
        key=str.lower
    )

    with open("usernames.txt", "w", encoding="utf-8") as f:
        for username in usernames:
            f.write(username + "\n")

    # =========================
    # members.csv
    # =========================

    with open(
        "members.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "username",
                "first_name",
                "last_name",
            ]
        )

        writer.writeheader()

        for member in members:
            writer.writerow(member)

    print()
    print("Готово!")
    print(f"Участников: {len(members)}")
    print(f"С username: {len(usernames)}")
    print("Файл с никами: usernames.txt")
    print("Полный файл: members.csv")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
