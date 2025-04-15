import asyncio
import subprocess
import logging

class OllamaService:
    def __init__(self, model_name):
        self.model_name = model_name

    # import subprocess
    
    def get_sql_query(self,prompt):
        try:
            process = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt,
                capture_output=True,
                text=True,
            )
            error = process.stderr
            if error:
                logging.error(f"olla error in ollama services {error}")
            return process.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Error calling Ollama: {e}")
            return None


        except Exception as e:
                logging.exception(f"Error calling Ollama {error}")
                return ""
