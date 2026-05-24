from modules.gemini_helper import ask_gemini
from modules.long_summarizer import compress_transcript


def extract_action_items(transcript):

    # Auto compress if transcript is too long
    if len(transcript) > 5000:
        transcript = compress_transcript(transcript)

    prompt = f"""
    Extract action items from this meeting.

    Return in format:

    Task:
    Owner:
    Deadline:

    Rules:
    - Keep formatting clean
    - If deadline missing write "Not specified"

    Transcript:
    {transcript}
    """

    return ask_gemini(prompt)