
import asyncio
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


from fastapi import FastAPI, Request
from services.database_service import DatabaseService
from services.ollama_service import OllamaService
from services.prompt_service import PromptService
from utils.sql_sanitizer import is_safe_sql
from Configurations import OLLAMA_MODEL
import logging

app = FastAPI()
db_service = DatabaseService()
ollama_service = OllamaService(OLLAMA_MODEL)

@app.on_event("startup")
async def startup():
    await db_service.init_pool()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question")
    print(question)

    prompt = PromptService.build_prompt(question)
    # print(prompt,"prompts")
    sql_query = ollama_service.get_sql_query(prompt)

    if not sql_query:
        return {"error": "Failed to generate SQL query"}

    if not is_safe_sql(sql_query):
        logging.warning(f"Unsafe SQL detected: {sql_query}")
        return {"error": "Unsafe query detected. Aborting."}

    db_result = await db_service.execute_query(sql_query)

    if db_result is None:
        return {"error": "Database query failed"}

    return {"query": sql_query, "result": db_result}
