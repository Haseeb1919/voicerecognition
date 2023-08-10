# `pip3 install assemblyai` (macOS)

import assemblyai as aai

aai.settings.api_key = "accf5ea8a6e94af2bdfba0ee795cfb94"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)