import os
import asyncio
import qrcode

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")


async def main():
    client = TelegramClient(
        "telegram_session",
        API_ID,
        API_HASH,
        device_model="Linux PC",
        system_version="Linux",
        app_version="1.0",
    )

    await client.connect()

    if await client.is_user_authorized():
        print("✅ Аккаунт уже авторизован!")

        me = await client.get_me()
        print(
            f"Аккаунт: {me.first_name or ''} "
            f"@{me.username or 'нет username'}"
        )
        print(f"ID: {me.id}")

        await client.disconnect()
        return

    print("Создаю QR-код...")
    qr = await client.qr_login()

    print()
    print("Отсканируй QR-код в Telegram:")
    print("Телефон → Настройки → Устройства → Подключить устройство")
    print()

    qr_code = qrcode.QRCode(border=1)
    qr_code.add_data(qr.url)
    qr_code.make(fit=True)
    qr_code.print_ascii(invert=True)

    print()
    print("Ожидаю подтверждение...")

    try:
        await qr.wait()

    except SessionPasswordNeededError:
        print()
        password = input(
            "Введи пароль двухэтапной аутентификации (2FA): "
        )
        await client.sign_in(password=password)

    print()
    print("✅ УСПЕШНО АВТОРИЗОВАНО!")

    me = await client.get_me()

    print(f"Имя: {me.first_name or ''}")
    print(
        f"Username: @{me.username}"
        if me.username
        else "Username: нет"
    )
    print(f"ID аккаунта: {me.id}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
