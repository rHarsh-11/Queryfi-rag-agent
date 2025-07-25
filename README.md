---

# 💡 QueryFi RAG Agent

A Natural Language Cross-Platform Data Query Agent that lets users query both MongoDB and MySQL using simple English. Built using LangChain, ReactJS, FastAPI, and OpenAI.

---

## 📌 Features

* 🔍 **Natural Language to MongoDB & MySQL**: Query both databases using plain English
* 🧠 **RAG Pipeline with LangChain**: Translates user queries into valid database queries
* 🌐 **ReactJS Frontend**: Simple UI for input and displaying structured results
* ⚙️ **FastAPI Backend**: Handles query parsing, LLM interaction, and DB connection
* 🛢️ **MongoDB & MySQL**: Supports read operations across both databases

---

## 🧱 Tech Stack

* 🧠 LangChain (RAG)
* 🐍 Python + FastAPI
* ⚛️ ReactJS
* 🐬 MySQL (Dockerized)
* 🍃 MongoDB (Atlas Cloud)
* 🤖 OpenAI (for query parsing)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Project

```bash
git clone https://github.com/rHarsh-11/valuefy-rag-agent.git
cd valuefy-rag-agent
```

---

## 🔧 Backend Setup (FastAPI)

### 2️⃣ Environment Variables

Create a `.env` file inside the `backend/` folder:

```bash
touch backend/.env
```

Paste the following into `backend/.env` and replace values accordingly:

```env
# MongoDB
MONGO_URI=mongodb+srv://<username>:<password>@valuefy.<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=valuefy
MONGO_DB_NAME=valuefy
MONGO_COLLECTION_NAME=clients

# MySQL
MYSQL_HOST=localhost
MYSQL_PORT=3307
MYSQL_USER=root
MYSQL_PASSWORD=rootpass
MYSQL_DATABASE=valuefy

# OpenAI
OPENAI_API_KEY=your_openai_api_key_here
```

### 3️⃣ Install Dependencies and Run

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🖥️ Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

If you want to use environment variables (e.g., backend URL) in React, create a `.env` file in `frontend/`:

```env
REACT_APP_API_URL=http://localhost:8000
```

---

## 🐬 MySQL Setup via Docker

```bash
docker run --name valuefy-mysql \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=valuefy \
  -p 3307:3306 \
  -d mysql:latest

# Load sample data
docker cp init_valuefy.sql valuefy-mysql:/init_valuefy.sql
docker exec -i valuefy-mysql mysql -uroot -prootpass valuefy < /init_valuefy.sql
```

---

## 📂 Folder Structure

```
valuefy-rag-agent/
│
├── backend/             # FastAPI backend for query routing and DB calls
│   ├── main.py
│   ├── .env             # Environment variables for MongoDB, MySQL, OpenAI
│   └── utils/
│
├── frontend/            # ReactJS frontend interface
│   ├── src/
│   ├── .env             # Optional: frontend environment (e.g. API URL)
│   └── public/
│
├── init_valuefy.sql     # Sample MySQL data
└── README.md
```

---

## 🧪 Example Queries

* "Show me all clients managed by RM2"
* "List all transactions where value is above 20 lakhs"
* "Who bought more than 100 units of stock?"

---

