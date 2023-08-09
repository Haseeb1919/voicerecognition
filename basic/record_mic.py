import pyaudio
import wave

#defing the parameters
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000



#initializing the pyaudio
p = pyaudio.PyAudio()
Stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Recording started")


#recording the frames
seconds = 5 #recording time
frames = [] #for storing the frames
for i in range (0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = Stream.read(FRAMES_PER_BUFFER)
    frames.append(data)



Stream.stop_stream()
Stream.close()
p.terminate()

#saving the file
obj = wave.open('recorded.wav','wb') #open new file
#setting the parameters of the file
obj.setnchannels(CHANNELS) #set channels
obj.setsampwidth(p.get_sample_size(FORMAT)) #set channels
obj.setframerate(RATE) #set frame rate
obj.writeframes(b''.join(frames)) #write frames
obj.close() #close the file
