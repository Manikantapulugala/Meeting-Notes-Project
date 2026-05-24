from modules.gemini_helper import ask_gemini


def compress_transcript(transcript):

    prompt = f"""
    You are a professional meeting analyzer.

    Your task is to compress this meeting transcript.

    KEEP ONLY:
    - Important discussion points
    - Technical details
    - Decisions taken
    - Issues/problems discussed
    - Tasks assigned
    - Deadlines
    - Risks/blockers

    REMOVE:
    - Small talk
    - Greetings
    - Repeated content
    - Filler words
    - Unimportant discussion

    Return only the important condensed transcript.

    Transcript:
    {transcript}
    """

    return ask_gemini(prompt)