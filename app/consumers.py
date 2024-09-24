import asyncio
import json
import aiohttp
from channels.generic.websocket import AsyncWebsocketConsumer
from google.cloud import speech
from asterisk.ami import AMIClient, AMIClientAdapter


# class SpeechToTextConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data=None, bytes_data=None):
#         if bytes_data:
#             transcript = await self.process_audio(bytes_data)
#             print(transcript)
#             await asyncio.sleep(5)

#             await self.send(text_data=json.dumps({
#                 'transcript': transcript
#             }))

#     async def process_audio(self, audio_data):
#         client = speech.SpeechClient()

#         audio = speech.RecognitionAudio(content=audio_data)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=8000,  # Asterisk often uses 8kHz for calls
#             language_code="uz-UZ",  # Uzbek language code
#             enable_automatic_punctuation=True,  # Optional: Enables punctuation
#         )
        
#         # Increased duration by adding long audio streaming support
#         response = client.long_running_recognize(config=config, audio=audio)
#         result = response.result(timeout=90)  # Wait for the response for a longer duration

#         if result.results:
#             return result.results[0].alternatives[0].transcript
#         return "Transkrip mavjud emas"



class SpeechToTextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            transcript = await self.process_audio(bytes_data)
            print(transcript)
            await asyncio.sleep(5)

            await self.send(text_data=json.dumps({
                'transcript': transcript
            }))

    async def process_audio(self, audio_data):
        url = 'https://back.aisha.group/stt_app/stt/post/'

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=audio_data) as response:
                if response.status == 200:
                    response_data = await response.json()
                    transcript = response_data.get('transcript', 'Transkrip mavjud emas')
                    return transcript
                else:
                    return f"Error: {response.status} - {await response.text()}"
