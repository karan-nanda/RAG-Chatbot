import re
import fitz
from llama_index.core import Document, Settings
from llama_index.core.schema import BaseNode
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
from typing import List, Any
from tqdm import tqdm
from ...setting import RAGSettings


load_dotenv()

class LocalDataIngestion:
    def __init__(self, setting: RAGSettings | None = None) -> None:
        self._setting = setting or RAGSettings()
        self._node_store = {}
        self._ingested_file = []
        
        
    def _filter_text(self, text):
        # Define the regex pattern.
        pattern = r'[a-zA-Z0-9 \u00C0-\u01B0\u1EA0-\u1EF9`~!@#$%^&*()_\-+=\[\]{}|\\;:\'",.<>/?]+'
        matches = re.findall(pattern, text)
        
        # Join all matched substrings into a single string
        filtered_text = ' '.join(matches)
        
        # Normalize the text by removing extra whitespaces
        normalized_text = re.sub(r'\s+', ' ', filtered_text.strip())

        return normalized_text
    
    def store_nodes(self,
                input_files: list[str],
                embed_nodes: bool = True,
                embed_model : Any | None= None) -> List[BaseNode]