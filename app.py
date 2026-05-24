import streamlit as st
from modules.transcriber import transcribe_audio
from modules.summarizer import generate_summary
from modules.action_items import extract_action_items
from modules.chroma_store import store_transcript
from modules.rag_chat import ask_question
from modules.utils import save_uploaded_file
import uuid

st.set_page_config(page_title="AI Meeting Notes", layout="wide")

st.title("AI Meeting Notes Assistant")

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(file_path)

    st.subheader("Transcript")
    st.write(transcript)

    with st.spinner("Generating summary..."):
        summary = generate_summary(transcript)

    st.subheader("Meeting Summary")
    st.write(summary)

    with st.spinner("Extracting action items..."):
        action_items = extract_action_items(transcript)

    st.subheader("Action Items")
    st.text(action_items)

    meeting_id = str(uuid.uuid4())

    store_transcript(
        meeting_id,
        transcript,
        summary,
        action_items
            )

    st.success("Meeting saved to ChromaDB")

st.divider()

st.subheader("Ask Questions About Past Meetings")
query = st.text_input("Ask anything")

if st.button("Ask") and query:
    answer = ask_question(query)
    st.write(answer)