ExportTgChatMembers

Небольшой скрипт для выгрузки username всех участников Telegram-чата.

Установка и запуск
Шаг 1. Клонируем репозиторий
git clone https://github.com/brenetoc/ExportTgChatMembers.git
cd ExportTgChatMembers

Шаг 2. Создаём и активируем виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate


После активации в начале строки терминала должно появиться:

(.venv)

Шаг 3. Устанавливаем зависимости
pip install -r requirements.txt

Шаг 4. Создаём .env

Создаём файл .env на основе примера:

cp .env.example .env


Открываем его:

nano .env


И заполняем своими данными:

API_ID=your_api_id
API_HASH=your_api_hash
CHAT_NAME=Название чата


CHAT_ID можно оставить пустым на этом этапе — получим его на следующем шаге.

Шаг 5. Авторизуем Telegram

Запускаем:

python qr_login.py


В терминале появится QR-код.


Шаг 6. Получаем ID чата

Запускаем:

python get_chatId.py


Скрипт найдёт чат по значению CHAT_NAME и выведет его ID. Копируем полученный ID и добавляем его в .env:

CHAT_ID=

Шаг 7. Выгружаем участников

python export_members.py




Они содержат приватные данные.

Они уже добавлены в .gitignore.
