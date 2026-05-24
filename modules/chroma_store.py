import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_PATH, COLLECTION_NAME, EMBEDDING_MODEL


client = chromadb.PersistentClient(path=CHROMA_PATH)

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_fn
)


def store_transcript(meeting_id, transcript, summary, action_items):
    collection.add(
        documents=[transcript],
        metadatas=[{
            "meeting_id": meeting_id,
            "summary": summary,
            "action_items": action_items
        }],
        ids=[meeting_id]
    )


def search_meetings(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results