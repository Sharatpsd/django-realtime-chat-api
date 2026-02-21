# 🚀 Django Real-Time Chat API

A backend-only real-time chat system with JWT authentication built using Django, Django REST Framework, and Django Channels.

This project demonstrates secure authentication, protected WebSocket communication, real-time message broadcasting, and database persistence.

---

## 📌 Features

- JWT Authentication (Register & Login)
- Password hashing using Django built-in authentication
- WebSocket connection protected with JWT validation
- Real-time chat using Django Channels
- Default chat room: `global`
- Message persistence (SQLite)
- Chat history endpoint
- Clean ASGI configuration using Daphne

---

## 🛠 Tech Stack

- Python 3.11
- Django 5.x
- Django REST Framework
- SimpleJWT
- Django Channels
- Daphne (ASGI Server)
- SQLite

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sharatpsd/django-realtime-chat-api.git
cd django-realtime-chat-api
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

---

## ▶️ Running the Project

### Run HTTP Server (API)

```bash
python manage.py runserver
```

### Run ASGI Server (WebSocket Support)

```bash
daphne config.asgi:application
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 🔐 Authentication Endpoints

### Register

**POST** `/api/register/`

Example Body:

```json
{
  "username": "testuser",
  "email": "test@test.com",
  "password": "12345678"
}
```

---

### Login

**POST** `/api/login/`

Response:

```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

## 🌐 WebSocket Connection

Connect using:

```
ws://127.0.0.1:8000/ws/chat/global/?token=ACCESS_TOKEN
```

Example (Browser Console):

```javascript
const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNjkzNDg0LCJpYXQiOjE3NzE2OTMxODQsImp0aSI6Ijc4OGZhM2Y4MzUxZjRhZDViMTU1N2Y3MmMxMTBiYjRmIiwidXNlcl9pZCI6IjEifQ.vTvFki40kE-XSLQnfIMSWKQeomYef-J8wLRWAnxZfMk";

const socket = new WebSocket(
  `ws://127.0.0.1:8000/ws/chat/global/?token=${token}`
);

socket.onopen = () => console.log("Connected!");
socket.onmessage = (e) => console.log("Message:", e.data);
socket.onerror = (e) => console.log("Error:", e);

socket.send(JSON.stringify({ message: "Hello world" }));
```

---

## 📜 Chat History Endpoint

**GET** `/api/chat/history/<room_name>/`

Header:

```
Authorization: Bearer ACCESS_TOKEN
```

Example:

```
GET /api/chat/history/global/
```

Response:

```json
[
  {
    "username": "testuser",
    "message": "Hello world",
    "timestamp": "2026-02-21T16:46:02Z"
  }
]
```

---


## 🧠 Architecture Overview

- JWT validated during WebSocket connection
- Anonymous users rejected
- Messages stored in database
- Room-based group broadcasting
- ASGI routing configured via `config/asgi.py`

---

## 📦 Deliverables Covered

✔ JWT Authentication  
✔ WebSocket Integration  
✔ Real-time Messaging  
✔ Data Persistence  
✔ Chat History Endpoint  
✔ Clean Project Structure  

---

## 👨‍💻 Author

Sharat Acharja  Mugdho 
sharatacharjee6@gmail.com
Backend Developer (Django)
