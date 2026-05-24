from modules.gemini_helper import ask_gemini
from modules.long_summarizer import compress_transcript


def generate_summary(transcript):

    # Auto compress if transcript is too long
    if len(transcript) > 5000:
        transcript = compress_transcript(transcript)

    prompt = f"""
    Summarize this meeting.

    Include:

    1. Key Discussion Points
    2. Decisions Taken
    3. Risks/Issues

    Transcript:
    {transcript}
    """

    return ask_gemini(prompt)