# 🧠 Natural Language to SQL Generator using LangChain & Ollama

This Streamlit application allows users to write natural language queries that are automatically converted into SQL statements using an LLM (`deepseek-r1:1.5b`) from the Ollama framework. It dynamically extracts the schema from a SQLite database and uses LangChain's prompt management to generate precise SQL queries.

---

## 🚀 Features

- ✅ Converts natural language questions into SQL queries
- ✅ Uses dynamic schema extraction from any SQLite database
- ✅ Powered by LangChain and Ollama LLM integration
- ✅ Clean, SQL-only output (no explanations or extra text)
- ✅ Simple web interface using Streamlit

---

## 🏗️ Project Structure

.
├── txt_to_sql.py # Main Streamlit application

├── testdb.sqlite # Sample SQLite database

├── images #for storing test run results screenshots

├── requirments.txt # to store the required library used in the project

└── README.md # Project documentation


---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone git@github.com:ratnesh134/Text-to-SQL-Generator.git
```

### 2. Create and Activate a Virtual Environment (Python 3.10+)

```bash
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Requirements

Make sure to include the following in your requirements.txt:

streamlit
langchain
langchain-core
langchain-ollama
sqlalchemy


Also, ensure you have Ollama installed locally and that the deepseek-r1:1.5b model is available.

## 💡 Usage
Run the app:

```bash

streamlit run txt_to_sql.py

```
Open the Streamlit interface in your browser.

Enter your natural language query (e.g., "Get all user names from the users table")

Copy the generated SQL code!

## 🧠 How it Works
The app reads the schema from a local SQLite database using SQLAlchemy.

It uses LangChain’s ChatPromptTemplate to inject the schema and question into a structured prompt.

The deepseek-r1:1.5b model from Ollama generates a raw response, which is cleaned to strip unnecessary text.

The final SQL query is displayed in a syntax-highlighted block.

## Sample Output 

![Alt text](https://github.com/ratnesh134/Text-to-SQL-Generator/blob/master/images/Screenshot%20from%202025-05-20%2020-47-23.png)

![Alt text](https://github.com/ratnesh134/Text-to-SQL-Generator/blob/master/images/Screenshot%20from%202025-05-20%2020-53-05.png)




