# ExportTgChatMembers
Легкий скриптик для выгрузки тг-ников всех участников чата 

ШАГ 1. Склонить репу и активировать .venv
source .venv/bin/activate

ШАГ 2. 
pip install -r requirements.txt

ШАГ 3. Создать .env и заполнить своими ключами
cp .env.example .env

ШАГ 4. Аторизация
python qr_login.py

ШАГ 5. Получаем ID чата и вставляем в .env в CHAT_ID
python get_chatId.py

ШАГ 6. 
python export_members.py
