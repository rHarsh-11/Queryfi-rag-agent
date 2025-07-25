import os
import re
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from query_router import execute_query_from_prompt
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4")

def extract_raw_query(response: str) -> str:
    """
    Extract the raw query text from the LLM response by removing markdown
    code blocks and labels like 'MySQL Query:', 'MongoDB Query:', etc.
    """
    code_block_pattern = re.compile(r"```(?:sql)?\s*(.*?)```", re.DOTALL | re.IGNORECASE)
    match = code_block_pattern.search(response)
    if match:
        return match.group(1).strip()

    cleaned = response
    for label in ["MySQL Query:", "MongoDB Query:"]:
        cleaned = cleaned.replace(label, "")
    return cleaned.strip()

def query_agent(user_question, model_name=OPENAI_MODEL):
    llm = ChatOpenAI(
        temperature=0,
        model_name=model_name,
        openai_api_key=OPENAI_API_KEY
    )

    prompt = f"""
You are an AI assistant for an investment platform.
Convert the following business question into a single SQL query or a single MongoDB query based on available schemas only — but not both.

Choose SQL if it relates to transactions data.  
Choose MongoDB if it relates to client profile data.

Only use these:

MySQL Table: transactions  
Columns: client_id, stock_name, units, value, relationship_manager, date

MongoDB Collection: clients  
Fields: name, risk_appetite, investment, relationship_manager

Do not invent table or column names. Just return one query based on the question.

Business question: {user_question}
"""
    print(f"\nPrompt to model:\n{prompt}")
    response = llm([HumanMessage(content=prompt)])
    print(f"\nModel response:\n{response.content}")

    structured_query = extract_raw_query(response.content)
    print(f"\nExtracted Structured Query:\n{structured_query}")

    result = execute_query_from_prompt(structured_query)
    return result
