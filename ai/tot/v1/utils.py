from langchain_openai.chat_models import ChatOpenAI


def get_model(model: str, temperature=1):
    if "gpt" in model:
        return ChatOpenAI(temperature=temperature, model=model)
    raise ValueError(f"No {model}")
