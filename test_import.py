import chromadb
import numpy as np
import uuid


def reproduce() -> None:
    entries = 1000
    random_vectors = np.random.rand(entries, 4096)
    client = chromadb.PersistentClient(path="test")
    collection = client.get_or_create_collection("my_collection")
    collection.add(ids=[f"{uuid.uuid4()}" for _ in range(entries)], documents=[f"document {i}" for i in range(entries)],
                   embeddings=random_vectors.tolist())
    print("Added 1000 documents to collection")


if __name__ == "__main__":
    reproduce()
