import sqlite3
from langchain.tools import Tool

connect = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    c = connect.cursor()
    c.execute(query)
    return c.fetchall()


run_query_tool = Tool.from_function(name="run_sqlite_query", description="Run a sqlite query.", func=run_sqlite_query)
