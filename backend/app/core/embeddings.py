from __future__ import annotations

from functools import lru_cache
from typing import List

from langchain_core.embeddings import Embeddings

from app.config import get_settings


class _FastEmbedWrapper(Embeddings):
    """用 fastembed 原生 API 包装成 LangChain Embeddings 接口。

    绕过 langchain-community 的 FastEmbedEmbeddings（即将废弃），
    直接调用 fastembed 自身，不依赖任何中间层。
    """

    def __init__(self, model_name: str) -> None:
        from fastembed import TextEmbedding  # noqa: PLC0415
        self._model = TextEmbedding(model_name=model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [vec.tolist() for vec in self._model.embed(texts)]

    def embed_query(self, text: str) -> List[float]:
        return next(self._model.embed([text])).tolist()


@lru_cache(maxsize=1)
def get_embeddings() -> Embeddings:
    """返回 Embedding 模型单例（fastembed 直接封装，无 langchain-community 依赖）。

    使用 BAAI/bge-small-zh-v1.5：
    - 中英双语，向量维度 512；
    - ONNX Runtime 推理，首次运行自动下载到 ~/.cache/fastembed（约 50MB）；
    - 无需 PyTorch，无需任何 API Key。
    """

    settings = get_settings()
    return _FastEmbedWrapper(model_name=settings.embedding_model)

