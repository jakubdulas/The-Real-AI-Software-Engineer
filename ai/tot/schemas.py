from pydantic import BaseModel


class ThoughtSchema(BaseModel):
    thought: str
    finish: bool
