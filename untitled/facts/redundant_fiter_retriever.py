from abc import ABC

from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema.retriever import BaseRetriever


class RedundantFilterRetriever(BaseRetriever, ABC):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # 쿼리 스트링의 임베딩 계산
        emb = self.embeddings.embed_query(query)

        # 임베딩을 이용해 max_marginal_relevance_search_vector 계산
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )

    async def aget_relevant_documents(self):
        return []
