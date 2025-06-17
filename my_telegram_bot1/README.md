# 🤖 Telegram Bot: Sticker & Google Drive

Простой Telegram-бот на Python с поддержкой:
- 📸 генерации стикеров из фото
- 💬 базового общения
- 🧠 кнопок-ответов
- ☁️ (в разработке) загрузки файлов в Google Drive

---

## 🚀 Запуск

1. Клонируй проект:

```bash
git clone https://github.com/your-username/telegram-bot.git
cd telegram-bot

Создай виртуальное окружение и активируй его:

bash
Копировать
Редактировать
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Установи зависимости:

bash
Копировать
Редактировать
pip install python-telegram-bot
Укажи токен бота в bot.py:

python
Копировать
Редактировать
app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
Запусти бота:

bash
Копировать
Редактировать
python bot.py