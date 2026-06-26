import chromadb
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter

from config import (
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

client = chromadb.PersistentClient(path=CHROMA_PATH)

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_fn
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)


def store_transcript(meeting_id, transcript, summary, action_items):

    chunks = text_splitter.split_text(transcript)

    documents = []
    metadatas = []
    ids = []

    for i, chunk in enumerate(chunks):
        documents.append(chunk)

        metadatas.append({
            "meeting_id": meeting_id,
            "summary": summary,
            "action_items": action_items,
            "chunk_id": i
        })

        ids.append(f"{meeting_id}_{i}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )


def search_meetings(query, n_results=3):
    return collection.query(
        query_texts=[query],
        n_results=n_results
    )
