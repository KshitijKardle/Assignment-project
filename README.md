# Django Internship Assignment

This project was developed as part of a Django internship assignment to demonstrate backend development skills, including API development, authentication, Celery background tasks, Telegram bot integration, and clean code management.

---

## 🔧 Tech Stack

- **Python 3.12**
- **Django 4.x**
- **Django REST Framework**
- **JWT Authentication**
- **Celery + Redis**
- **Telegram Bot**
- **PostgreSQL / SQLite**
- **Environment Variables via `python-decouple`**

---

## 🚀 Features Implemented

- ✅ Django Project Setup
- ✅ REST API with Public & Protected Endpoints
- ✅ JWT Token Authentication
- ✅ User Registration via Web
- ✅ Celery Task: Send Welcome Email after Registration
- ✅ Telegram Bot Integration
- ✅ Telegram `/start` command stores user to DB
- ✅ Login via Web Interface

---

## 🧪 API Endpoints

| Method   | URL                   | Access        | Description                 |
| -------- | --------------------- | ------------- | --------------------------- |
| GET      | `/api/public/`        | Public        | Returns a public message    |
| GET      | `/api/protected/`     | JWT/Auth Only | Returns a protected message |
| POST     | `/api/token/`         | Public        | Get access + refresh token  |
| POST     | `/api/token/refresh/` | Public        | Refresh access token        |
| GET/POST | `/register/`          | Public        | Register new user           |

---

## 🧵 Telegram Bot

- Bot created via [@BotFather](https://t.me/BotFather)
- `/start` command stores user's Telegram username and ID to the database
- Uses `python-telegram-bot` with `async` and `sync_to_async`

---

## 📨 Celery + Redis

- Celery task sends a welcome email after registration
- Broker: Redis (`redis://localhost:6379/0`)

**Run Redis:**

```bash
redis-server
```

**Start Celery Worker:**

```bash
celery -A assignment worker --loglevel=info --pool=solo
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/KshitijKardle/Assignment-project
   cd Assignment-project
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv .venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Set up `.env` file**  
   Create a `.env` file in the project root with:

   ```env
   SECRET_KEY=your-django-secret
   DEBUG=False
   ALLOWED_HOSTS=127.0.0.1,localhost

   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password

   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   ```

4. **Run the Django app**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### How to Use

Go to account/register/ to create an account

Log in via /accounts/login/

Access /api/public/ and /api/protected/

Talk to your Telegram bot → /start
