from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.schema.messages import SystemMessage

from dotenv import load_dotenv
from tools.sql import run_query_tool, list_tables, describe_tables_tool

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()

prompt = ChatPromptTemplate(messages=[
    SystemMessage(content=("You are an AI that has access to a SQLite database.\n"
                          f"The database has tables of : {tables}\n"
                          "Do not make any assumptions about what tables exist "
                          "or what columns exist. Instead, use the 'describe_tables' function")),
    HumanMessagePromptTemplate.from_template("{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

tools = [run_query_tool, describe_tables_tool]

agent = OpenAIFunctionsAgent(llm=chat, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

agent_executor("How many users have provided a shipping address?")
