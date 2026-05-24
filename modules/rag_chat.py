from modules.chroma_store import search_meetings
from modules.gemini_helper import ask_gemini


def ask_question(query):
    results = search_meetings(query)

    context = "".join(results["documents"][0])

    prompt = f"""
    Use the meeting context below to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    return ask_gemini(prompt)