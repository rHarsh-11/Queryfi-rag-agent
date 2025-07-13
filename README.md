# 💡 Valuefy RAG Agent

A Natural Language Cross-Platform Data Query Agent that lets users query both MongoDB and MySQL using simple English. Built using LangChain, ReactJS, FastAPI, and OpenAI.

---

## 📌 Features

- 🔍 **Natural Language to MongoDB & MySQL**: Query both databases using plain English
- 🧠 **RAG Pipeline with LangChain**: Translates user queries into valid database queries
- 🌐 **ReactJS Frontend**: Simple UI for input and displaying structured results
- ⚙️ **FastAPI Backend**: Handles query parsing, LLM interaction, and DB connection
- 🛢️ **MongoDB & MySQL**: Supports read operations across both databases

---

## 🧱 Tech Stack

- 🧠 LangChain (RAG)
- 🐍 Python + FastAPI
- ⚛️ ReactJS
- 🐬 MySQL (Dockerized)
- 🍃 MongoDB (Atlas Cloud)
- 🧠 OpenAI (for query parsing)

---

## ⚙️ Setup Instructions

### Clone the project
```bash
git clone https://github.com/rHarsh-11/valuefy-rag-agent.git
```` 

### 🔧 Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
````

### 🖥️ Frontend (React)

```bash
cd frontend
npm install
npm start
```

### 🐬 MySQL via Docker

```bash
docker run --name valuefy-mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=valuefy -p 3307:3306 -d mysql:latest
docker cp init_valuefy.sql valuefy-mysql:/init_valuefy.sql
docker exec -i valuefy-mysql mysql -uroot -prootpass valuefy < /init_valuefy.sql
```

---

## 📂 Folder Structure

```
valuefy-rag-agent/
│
├── backend/           # FastAPI backend for query routing and DB calls
│   ├── main.py
│   └── utils/
│
├── frontend/          # ReactJS frontend interface
│   ├── src/
│   └── public/
│
├── init_valuefy.sql   # Sample MySQL data
└── README.md
```

---

## 🧪 Example Queries

* "Show me all clients managed by RM2"
* "List all transactions where value is above 20 lakhs"
* "Who bought more than 100 units of stock?"

```
