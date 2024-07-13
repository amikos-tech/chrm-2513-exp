import chromadb
import numpy as np
import uuid


def reproduce() -> None:
    random_vectors = np.random.rand(100, 1024)
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection("my_collection")
    collection.add(ids=[f"{uuid.uuid4()}" for _ in range(1000)], documents=[f"document {i}" for i in range(1000)], embeddings=random_vectors.tolist())
    print("Added 1000 documents to collection")

if __name__ == "__main__":
    reproduce()
