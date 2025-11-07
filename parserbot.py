import sqlite3
import re
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "YOUR_BOT_API_TOKEN"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_NAME = 'parser_bot.db'

def init_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keywords (
            user_id INTEGER,
            keyword TEXT,
            PRIMARY KEY (user_id, keyword)
        )
    ''')
    conn.commit()
    conn.close()

def get_user_keywords(user_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT keyword FROM keywords WHERE user_id = ?', (user_id,))
    keywords = [row[0] for row in cursor.fetchall()]
    conn.close()
    return keywords

def add_user_keyword(user_id, keyword):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO keywords (user_id, keyword) VALUES (?, ?)', (user_id, keyword.lower()))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def remove_user_keyword(user_id, keyword):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM keywords WHERE user_id = ? AND keyword = ?', (user_id, keyword.lower()))
    conn.commit()
    conn.close()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Бот-парсер сообщений\n\n"
        "Команды:\n"
        "/add keyword - добавить ключевое слово\n"
        "/remove keyword - удалить ключевое слово\n"
        "/list - показать мои ключевые слова\n"
        "/clear - очистить все ключевые слова\n\n"
        "Бот будет присылать вам сообщения из чатов, содержащие ваши ключевые слова."
    )

async def add_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово: /add слово")
        return
    
    keyword = ' '.join(context.args).lower()
    user_id = update.effective_user.id
    
    add_user_keyword(user_id, keyword)
    await update.message.reply_text(f"✅ Ключевое слово '{keyword}' добавлено")

async def remove_keyword_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите ключевое слово: /remove слово")
        return
    
    keyword = ' '.join(context.args).lower()
    user_id = update.effective_user.id
    
    remove_user_keyword(user_id, keyword)
    await update.message.reply_text(f"✅ Ключевое слово '{keyword}' удалено")

async def list_keywords_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    keywords = get_user_keywords(user_id)
    
    if not keywords:
        await update.message.reply_text("📝 У вас нет ключевых слов. Добавьте их командой /add")
        return
    
    keywords_list = "\n".join([f"• {keyword}" for keyword in keywords])
    await update.message.reply_text(f"📝 Ваши ключевые слова:\n{keywords_list}")

async def clear_keywords_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM keywords WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    await update.message.reply_text("✅ Все ключевые слова очищены")

async def handle_group_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    message_text = update.message.text.lower()
    chat_title = update.effective_chat.title
    message_link = f"https://t.me/c/{str(update.effective_chat.id)[4:]}/{update.message.message_id}"

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT user_id FROM keywords')
    users = [row[0] for row in cursor.fetchall()]
    conn.close()

    for user_id in users:
        user_keywords = get_user_keywords(user_id)
        found_keywords = []
        
        for keyword in user_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', message_text):
                found_keywords.append(keyword)

        if found_keywords:
            notification = (
                f"🔍 Найдено совпадение в чате '{chat_title}'\n"
                f"Ключевые слова: {', '.join(found_keywords)}\n"
                f"Сообщение: {update.message.text[:300]}...\n"
                f"Ссылка: {message_link}"
            )
            
            try:
                await context.bot.send_message(chat_id=user_id, text=notification)
            except Exception as e:
                logger.error(f"Не удалось отправить уведомление пользователю {user_id}: {e}")

def main():
    init_database()
    
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("add", add_keyword_command))
    application.add_handler(CommandHandler("remove", remove_keyword_command))
    application.add_handler(CommandHandler("list", list_keywords_command))
    application.add_handler(CommandHandler("clear", clear_keywords_command))
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS & ~filters.COMMAND, handle_group_message))

    application.run_polling()

if __name__ == "__main__":
    main()