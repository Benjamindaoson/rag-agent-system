from __future__ import annotations

from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.config import get_settings


def get_llm(*, streaming: bool = False, temperature: float = 0.1) -> BaseChatModel:
    """返回项目统一使用的聊天模型实例。

    当前使用 DeepSeek（通过 OpenAI 兼容接口接入）。
    业务层依赖 BaseChatModel 抽象类型，后续切换其他 LLM 只需改这里。
    """

    settings = get_settings()
    return ChatOpenAI(
        model=settings.model,
        api_key=settings.llm_api_key,          # type: ignore[arg-type]
        base_url=settings.llm_base_url,
        streaming=streaming,
        temperature=temperature,
    )
