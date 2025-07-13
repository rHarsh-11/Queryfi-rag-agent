from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_agent import query_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def handle_query(req: QueryRequest):
    try:
        result = query_agent(req.question)
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
