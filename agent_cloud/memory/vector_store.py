import os
import weaviate
from typing import List, Dict, Any

class LongTermMemoryVectorStore:
    """
    Enterprise-grade Vector Database connection for Agent Long-Term Memory.
    Utilizes Weaviate to store episodic memories, spatial graphs, and learned skills.
    """
    def __init__(self):
        weaviate_url = os.getenv("VECTOR_DB_URL", "http://localhost:8080")
        self.client = weaviate.Client(
            url=weaviate_url,
            additional_headers={
                "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY", "")
            }
        )
        self._ensure_schema()

    def _ensure_schema(self):
        class_obj = {
            "class": "EpisodicMemory",
            "description": "Stores the agent's experiences and environmental observations",
            "vectorizer": "text2vec-openai",
            "properties": [
                {
                    "name": "timestamp",
                    "dataType": ["date"],
                },
                {
                    "name": "content",
                    "dataType": ["text"],
                },
                {
                    "name": "spatial_context",
                    "dataType": ["text"],
                }
            ]
        }
        if not self.client.schema.exists("EpisodicMemory"):
            self.client.schema.create_class(class_obj)

    def store_memory(self, content: str, spatial_context: str):
        data_object = {
            "content": content,
            "spatial_context": spatial_context,
            "timestamp": "2024-01-01T00:00:00Z" # In real app, use datetime.utcnow().isoformat() + "Z"
        }
        self.client.data_object.create(
            data_object,
            "EpisodicMemory"
        )

    def retrieve_relevant_context(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        result = (
            self.client.query
            .get("EpisodicMemory", ["content", "spatial_context"])
            .with_near_text({"concepts": [query]})
            .with_limit(limit)
            .do()
        )
        return result.get("data", {}).get("Get", {}).get("EpisodicMemory", [])
