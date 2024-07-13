import chromadb

import uuid


def reproduce() -> None:
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection("my_collection")

    collection.add(ids=[f"{uuid.uuid4()}" for _ in range(1000)], documents=[f"document {i}" for i in range(1000)])


if __name__ == "__main__":
    reproduce()
