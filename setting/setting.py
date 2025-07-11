from pydantic import BaseModel, Field
from typing import List


class OllamaSettings(BaseModel):
    llm : str = Field(
        default='llama3:8b-instruct-q8_0', description="LLM model"
    )
    keep_alive: str = Field(
        default="1h", description="Keep alive time for the server"
    )
    tfs_z: float = Field(
        default = 1.0, description="TFS normalization factor"
    )
    top_k: int = Field(
        default=40, description="Top k sampling"
    )
    top_p: float = Field(
        default=0.9, description="Top p sampling"
    )
    repeat_last_n: int = Field(
        default=64, description= "Repeat last n tokens"
    )
    repeat_penalty: float = Field(
        default=1.1 , description="Repeat penalty"
    )
    request_timeout: float = Field(
        default=300, description="Request timeout"
    )
    port : int = Field(
        default=11434, description="Port number"
    )
    context_window: int = Field(
        default=8000, description="Context window size"
    )
    temperature : float = Field(
        default=0.1, description="Temperature"
    )
    chat_token_limit: int = Field(
        default=4000, description="Chat memory limit"
    )
    
