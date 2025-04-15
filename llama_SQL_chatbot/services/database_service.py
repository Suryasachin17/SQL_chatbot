import asyncmy
import asyncio
import logging
from Configurations import DB_CONFIG, RETRY_ATTEMPTS, RETRY_DELAY
from utils.sql_sanitizer import extract_sql
from asyncmy.errors import OperationalError
class DatabaseService:
    def __init__(self):
        self.pool = None

    async def init_pool(self):
        self.pool = await asyncmy.create_pool(
            **DB_CONFIG,
            autocommit=True
        )
        logging.info("Database connection pool created.")


    async def execute_query(self, query: str):
        attempt = 0
        
        while attempt < RETRY_ATTEMPTS:
            try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cursor:
                        print("start*******",query,"*****check query",extract_sql(query))
                        await cursor.execute(query)
                        # print(query,"check query")
                        result = await cursor.fetchall()
                        print(result,"check query")
                        logging.info(f"DB Query Success: {query}")
                        return result

            except OperationalError as e:
                logging.warning(f"DB OperationalError: {e} - Attempt {attempt + 1}")
                attempt += 1
                await asyncio.sleep(RETRY_DELAY)

            except Exception as e:
                logging.exception(f"DB Unexpected Error: {e}")
                break

        logging.error(f"DB Query failed after {RETRY_ATTEMPTS} attempts: {query}")
        return None
