import sqlite3
from langchain.tools import Tool

connect = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    c = connect.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occured: {str(err)}"


run_query_tool = Tool.from_function(name="run_sqlite_query", description="Run a sqlite query.", func=run_sqlite_query)
