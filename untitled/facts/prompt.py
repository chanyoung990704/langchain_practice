from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models.openai import ChatOpenAI
from redundant_fiter_retriever import RedundantFilterRetriever
from dotenv import load_dotenv
import langchain

langchain.debug = True

load_dotenv()

chat = ChatOpenAI()
ai_embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="emb", embedding_function=ai_embeddings)
retriever = RedundantFilterRetriever(embeddings=ai_embeddings, chroma=db)

# retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(llm=chat, retriever=retriever, chain_type="refine")

result = chain.run("what is an interesting fact about English language?")
print(result)
