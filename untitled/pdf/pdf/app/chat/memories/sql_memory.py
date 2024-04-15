from pydantic import BaseModel, Field
from typing import List
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory

from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

class Message(BaseModel):
    content: str

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str
    messages: List[Message] = Field(..., alias="messages")

    @classmethod
    def model_rebuild(cls):
        cls.__annotations__["messages"] = List[Message]

    def get_messages(self):
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )

    def clear(self):
        pass

# Ensure the model is fully defined
SqlMessageHistory.model_rebuild()

def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id,
            messages=[]
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
