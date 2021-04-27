
def create_table_query():
    return """CREATE TABLE IF NOT EXISTS fortunes (id SERIAL PRIMARY KEY,fortune TEXT)"""


def insert_rows_query():
    return """INSERT INTO fortunes (fortune) VALUES(%s)"""


def get_fortune_query():
    return """SELECT id, fortune FROM fortunes ORDER BY RANDOM() LIMIT 1"""


def save_fortune_query():
    return """UPDATE fortunes SET fortune = %s WHERE id = %s"""
