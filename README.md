# Telegram Parser Bot 🔍

[English](#english) | [Русский](#russian)

---

## English {#english}

> ⚠️ **Project Status**: Completed  
> Telegram bot for monitoring group chats and notifying users about messages containing their keywords.

### Overview

A Telegram bot designed to monitor group chats and send personalized notifications to users when messages contain their specified keywords. Perfect for brand monitoring, topic tracking, and staying updated on relevant discussions.
m

### Features

#### 🔍 Core Functionality
- **Keyword Monitoring** - Track specific words and phrases in group chats
- **Real-time Notifications** - Instant alerts when keywords are detected
- **Multi-user Support** - Each user manages their own keyword list
- **Group Chat Coverage** - Monitors all groups where bot is added

#### ⚙️ Management System
- **Personal Keyword Lists** - Unique keywords per user
- **Easy Management** - Simple commands to add/remove keywords
- **Case-insensitive Search** - Finds matches regardless of capitalization
- **Exact Word Matching** - Uses word boundaries for precise results

#### 📊 Notification System
- **Detailed Alerts** - Chat name, matched keywords, message preview
- **Direct Message Delivery** - Notifications sent to private chat
- **Message Links** - Direct link to original message
- **Smart Filtering** - Ignores bot commands in groups

### Technology Stack

- **Python 3.x**
- **python-telegram-bot** - Telegram Bot API wrapper
- **SQLite3** - Database for user keywords
- **Regex** - Advanced text pattern matching
- **Logging** - Comprehensive event tracking

### Installation

1. **Clone repository**
```bash
git clone https://github.com/1NC0SSAT0R/Telegram-Parser-Bot.git
cd Telegram-Parser-Bot
```

2. **Install dependencies**
```bash
pip install python-telegram-bot
```

3. **Configure bot**
   - Obtain Bot Token from [@BotFather](https://t.me/BotFather)
   - Replace `YOUR_BOT_API_TOKEN` in the code with your actual token

4. **Run bot**
```bash
python bot.py
```

### Commands Reference

| Command | Description |
|---------|-------------|
| `/start` | Bot introduction and commands list |
| `/add keyword` | Add keyword to monitoring list |
| `/remove keyword` | Remove keyword from list |
| `/list` | Show all your keywords |
| `/clear` | Clear all keywords |

### Usage Example

1. Add bot to your group chats
2. Send `/add python` to track mentions of Python
3. Receive notifications when "python" is mentioned in any monitored group
4. Use `/list` to see all tracked keywords
5. Use `/remove python` to stop tracking

### Business Applications

- **Brand Monitoring** - Track mentions of your company/product
- **Market Research** - Monitor discussions about specific topics
- **Community Management** - Stay updated on relevant conversations
- **Lead Generation** - Find potential customers discussing related services
- **Competitor Analysis** - Track mentions of competitor brands

### Project Structure

```
telegram-parser-bot/
├── bot.py              # Main bot implementation
├── parser_bot.db       # SQLite database (auto-generated)
└── README.md          # Documentation
```

### Features in Detail

**Smart Search:**
- Exact word matching with regex boundaries
- Case-insensitive detection
- Multiple keywords per user
- Real-time processing

**Database Scheme:**
```sql
keywords (
    user_id INTEGER,
    keyword TEXT,
    PRIMARY KEY (user_id, keyword)
)
```

### Contact

Developer: [Telegram](https://t.me/inc0bio)

---

## Русский {#russian}

> ⚠️ **Статус проекта**: Завершен  
> Telegram бот для мониторинга групповых чатов и уведомления пользователей о сообщениях, содержащих их ключевые слова.

### Обзор

Telegram бот для мониторинга групповых чатов и отправки персонализированных уведомлений пользователям при обнаружении их ключевых слов. Идеален для мониторинга бренда, отслеживания тем и получения актуальной информации об обсуждаемых вопросах.

### Функционал

#### 🔍 Основные возможности
- **Мониторинг ключевых слов** - Отслеживание specific слов и фраз в групповых чатах
- **Уведомления в реальном времени** - Мгновенные оповещения при обнаружении ключевых слов
- **Поддержка множества пользователей** - Каждый пользователь управляет своим списком слов
- **Покрытие групповых чатов** - Мониторинг всех групп, куда добавлен бот

#### ⚙️ Система управления
- **Персональные списки слов** - Уникальные ключевые слова для каждого пользователя
- **Простое управление** - Легкие команды для добавления/удаления слов
- **Регистронезависимый поиск** - Находит совпадения независимо от регистра
- **Точное совпадение слов** - Использует границы слов для точных результатов

#### 📊 Система уведомлений
- **Детальные оповещения** - Название чата, найденные слова, превью сообщения
- **Доставка в личные сообщения** - Уведомления отправляются в личный чат
- **Ссылки на сообщения** - Прямая ссылка на оригинальное сообщение
- **Умная фильтрация** - Игнорирует команды бота в группах

### Технологический стек

- **Python 3.x**
- **python-telegram-bot** - Обертка для Telegram Bot API
- **SQLite3** - База данных для ключевых слов пользователей
- **Regex** - Продвинутое сопоставление текстовых шаблонов
- **Logging** - Комплексное отслеживание событий

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/1NC0SSAT0R/Telegram-Parser-Bot.git
cd Telegram-Parser-Bot
```

2. **Установите зависимости**
```bash
pip install python-telegram-bot
```

3. **Настройте бота**
   - Получите токен бота у [@BotFather](https://t.me/BotFather)
   - Замените `YOUR_BOT_API_TOKEN` в коде на ваш реальный токен

4. **Запустите бота**
```bash
python bot.py
```

### Справочник команд

| Команда | Описание |
|---------|-------------|
| `/start` | Знакомство с ботом и список команд |
| `/add слово` | Добавить слово в список мониторинга |
| `/remove слово` | Удалить слово из списка |
| `/list` | Показать все ваши ключевые слова |
| `/clear` | Очистить все ключевые слова |

### Пример использования

1. Добавьте бота в ваши групповые чаты
2. Отправьте `/add python` для отслеживания упоминаний Python
3. Получайте уведомления при упоминании "python" в любом monitored чате
4. Используйте `/list` для просмотра всех отслеживаемых слов
5. Используйте `/remove python` чтобы прекратить отслеживание

### Бизнес-применение

- **Мониторинг бренда** - Отслеживание упоминаний вашей компании/продукта
- **Маркетинговые исследования** - Мониторинг обсуждений specific тем
- **Управление сообществом** - Будьте в курсе релевантных обсуждений
- **Генерация лидов** - Поиск потенциальных клиентов, обсуждающих related услуги
- **Анализ конкурентов** - Отслеживание упоминаний брендов конкурентов

### Структура проекта

```
telegram-parser-bot/
├── bot.py              # Основная реализация бота
├── parser_bot.db       # SQLite база данных (авто-генерация)
└── README.md          # Документация
```

### Особенности реализации

**Умный поиск:**
- Точное совпадение слов с границами regex
- Регистронезависимое обнаружение
- Несколько ключевых слов на пользователя
- Обработка в реальном времени

**Схема базы данных:**
```sql
keywords (
    user_id INTEGER,
    keyword TEXT,
    PRIMARY KEY (user_id, keyword)
)
```

### Контакты

Разработчик: [Telegram](https://t.me/inc0bio)
