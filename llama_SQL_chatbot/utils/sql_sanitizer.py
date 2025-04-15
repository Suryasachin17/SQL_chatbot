def is_safe_sql(query: str) -> bool:
    dangerous_statements = ['DROP', 'DELETE', 'TRUNCATE', 'ALTER']
    return not any(word in query.upper() for word in dangerous_statements)




def extract_sql(response_text):
    # Simple method: find the first SELECT / INSERT / UPDATE / DELETE
    lines = response_text.splitlines()
    for line in lines:
        if line.strip().lower().startswith(('select', 'insert', 'update', 'delete')):
            return line.strip()
    return None  # or raise an error

