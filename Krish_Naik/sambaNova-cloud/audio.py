import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


def translate_audio(audio_file_path, api_key, target_language):
    headers = {"Authorization": f"Bearer {api_key}"}

    files = {'file': open(audio_file_path, 'rb')}
      
    data = {
          'model': 'Whisper-Large-v3',
          'language': target_language,  
          'response_format': "text" ,
      }
    response = requests.post(
          "https://api.sambanova.ai/v1/audio/translations",
          headers=headers,
          files=files,
          data=data
      )
    if not response.ok:
        raise RuntimeError(f"{response.status_code}: {response.text}")
    return response.text

if __name__ == "__main__":
    api_key=os.getenv("SAMBANOVA_API_KEY")
    audio_file_path = "meeting-audio.mp4"  # Replace with your audio file path
    target_language = "english"  # Replace with your desired target language

    translation_result = translate_audio(audio_file_path, api_key, target_language)
    print(json.dumps(translation_result, indent=2))


