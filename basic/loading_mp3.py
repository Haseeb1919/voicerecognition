from pydub import AudioSegment

audio = AudioSegment.from_mp3("sample.mp3")
print("audio is loaded")

#increase the volume of the audio by 6 dB
audio = audio = 6

audio = audio * 2 