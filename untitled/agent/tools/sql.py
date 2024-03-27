import sqlite3
from langchain.tools import Tool

connect = sqlite3.connect("db.sqlite")


def list_tables():
    cursor = connect.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    c = connect.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occured: {str(err)}"


run_query_tool = Tool.from_function(name="run_sqlite_query", description="Run a sqlite query.", func=run_sqlite_query)

def describe_tables(table_names):
    cursor = connect.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name IN ({tables});")
    return "\n".join(row[0] for row in rows if row[0] is not None)

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables
)
