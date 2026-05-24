from modules.gemini_helper import model
import google.generativeai as genai
import time


def transcribe_audio(audio_path):
    retries = 3

    for attempt in range(retries):
        try:
            uploaded_file = genai.upload_file(audio_path)

            prompt = """
            Transcribe this meeting audio accurately.

            Rules:
            1. Return only transcript.
            2. Keep speaker labels if identifiable.
            3. Remove timestamps.
            4. Do not summarize.
            5. Preserve conversation flow.
            6. Do not invent speaker names.

            Example:

            Manager:
            Good morning everyone.

            Developer:
            I'll optimize SQL queries.
            """

            response = model.generate_content(
                [prompt, uploaded_file]
            )

            return response.text

        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")

            if attempt < retries - 1:
                time.sleep(5)
            else:
                raise e