from typing import Dict, Any, List, Optional
from uuid import UUID

from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        print(messages)