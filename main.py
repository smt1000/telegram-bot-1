import requests
from io import BytesIO

IMAGE_URL = "https://images.steamusercontent.com/ugc/965355694153811922/DF6B86B28B17363E7529D2980F1580D221B2B96D/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"

@bot.message_handler(commands=["start"])
def start(message):
    try:
        response = requests.get(IMAGE_URL, timeout=20)

        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question1.jpg"

        bot.send_photo(
            message.chat.id,
            photo
        )

    except Exception as e:
        print("IMAGE ERROR:", e)
        bot.send_message(
            message.chat.id,
            f"Image error: {e}"
        )
