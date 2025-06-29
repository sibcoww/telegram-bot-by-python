Вот полный текст, который ты можешь сразу вставить в `README.md` — **без форматирования командной строки** и лишних вставок:

---

# 🤖 Telegram Bot: Sticker & Google Drive

Простой Telegram-бот на Python с поддержкой:

* 📸 генерации стикеров из фото
* 💬 базового общения
* 🧠 кнопок-ответов
* ☁️ (в разработке) загрузки файлов в Google Drive

---

## 🚀 Запуск

1. Клонируй проект:

   * `git clone https://github.com/your-username/telegram-bot.git`
   * `cd telegram-bot`

2. Создай виртуальное окружение и активируй его:

   * `python -m venv venv`
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`

3. Установи зависимости:

   * `pip install python-telegram-bot`

4. Укажи токен бота в `bot.py`:

   ```python
   app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
   ```

5. Запусти бота:

   * `python bot.py`

---

## 📁 Структура проекта

* `bot.py` — основной код бота
* `.gitignore` — исключения для Git
* `README.md` — описание проекта
* `venv/` — виртуальное окружение (не добавляется в Git)
* `to_sticker.png` — временный файл стикера

---

## ⚠️ Важно

* Не загружай в репозиторий: `credentials.json`, `token.json`, `.env`, `venv/`
* Добавь их в `.gitignore` для безопасности
* Токен Telegram лучше хранить в `.env` (или использовать переменные окружения)

---

## 📌 Возможности

* `/start` — приветствие с кнопками
* `/help` — краткое руководство
* **Make a sticker** — бот ждёт фото и делает стикер
* **Use Google Drive** — (в разработке) загрузка на облако

---

## 🛠️ В планах

* Интеграция с Google Drive
* Инлайн-кнопки и реакции на нажатия
* Поддержка документов, голосовых, видео и других медиа

---

## 🧑‍💻 Автор

> Создан в образовательных целях — для изучения Python, Telegram Bot API и Google API.

---
