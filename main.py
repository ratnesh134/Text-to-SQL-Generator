import json
import re
import streamlit as st
import pandas as pd

from langchain_ollama.llms import OllamaLLM
from sqlalchemy import create_engine, inspect
from langchain_core.prompts import ChatPromptTemplate

# Database URL
db_url = "sqlite:///testdb.sqlite"

# Prompt template for the LLM
template = """
You are a SQL generator. When given a schema and a user question, you MUST output only the SQL statement—nothing else. No explanation is needed.

Schema: {schema}
User question: {query}
Output (SQL only):
"""

# Initialize the LLM
model = OllamaLLM(model="deepseek-r1:1.5b")

# Extract schema as a dictionary for visualization and as JSON for the prompt
def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}
    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        schema[table] = [col['name'] for col in columns]
    return schema

# Generate SQL from user query and schema
def to_sql_query(query, schema):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return clean_text(chain.invoke({"query": query, "schema": json.dumps(schema)}))

# Clean up LLM output
def clean_text(text: str):
    # Adjusted regex pattern to match and remove LLM thinking artifacts
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()

# Execute SQL and return results as a DataFrame
def run_sql(sql, db_url):
    engine = create_engine(db_url)
    try:
        df = pd.read_sql_query(sql, engine)
        return df, None
    except Exception as e:
        return None, str(e)

# --- Streamlit UI ---
st.title("🧠 Text to SQL Generator")

# Extract and show schema
schema = extract_schema(db_url)

with st.sidebar:
    st.header("📊 Database Schema")
    for table, columns in schema.items():
        st.markdown(f"**{table}**")
        st.markdown(", ".join(columns))

query = st.text_area("🗣️ Describe the data you want to retrieve from the database:")

if query:
    sql = to_sql_query(query, schema)
    st.subheader("🧾 Generated SQL")
    st.code(sql, wrap_lines=True, language="sql")

    if st.button("🚀 Run Query"):
        df, error = run_sql(sql, db_url)
        if error:
            st.error(f"❌ Error: {error}")
        elif df is not None and not df.empty:
            st.subheader("📈 Query Results")
            st.dataframe(df)
        else:
            st.info("✅ Query executed successfully, but returned no results.")
