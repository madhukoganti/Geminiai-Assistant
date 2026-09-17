import logging

from google import genai
from django.conf import settings


logger = logging.getLogger(__name__)


client = genai.Client(
    api_key=settings.GEMINIAI_API_KEY
)


def get_ai_response(user_message):

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                "You are a helpful AI assistant. "
                                "Answer clearly and simply.\n\n"
                                f"User: {user_message}"
                            )
                        }
                    ]
                }
            ]
        )

        if not response.text:

            logger.warning(
                "Gemini returned an empty response."
            )

            return (
                "Sorry, Gemini returned an empty response. "
                "Please try again."
            )

        return response.text


    except Exception as e:

        error_message = str(e).lower()


        logger.error(
            "Gemini API error: %s",
            e,
            exc_info=True
        )


        if "503" in error_message or "unavailable" in error_message:

            return (
                "Gemini is temporarily busy. "
                "Please try again in a few moments."
            )


        elif "401" in error_message or "403" in error_message:

            return (
                "There is a problem with the Gemini API "
                "authentication. Please check the API configuration."
            )


        elif "429" in error_message or "quota" in error_message:

            return (
                "Gemini API usage limit has been reached. "
                "Please try again later."
            )


        else:

            return (
                "Sorry, something went wrong while contacting Gemini. "
                "Please try again."
            )