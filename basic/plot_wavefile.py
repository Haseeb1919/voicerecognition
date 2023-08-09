import wave 
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open('conference.wav','rb') #open the file

sample_rate = obj.getframerate() #get the sample rate
total_frames = obj.getnframes() #get the total frames
signal = obj.readframes(-1) #read the frames

obj.close() #close the file

audio_time = total_frames / float(sample_rate) #get the total time
print("Audio time",audio_time)


#convert the frames into integers
signal = np.frombuffer(signal,dtype='int16')
time = np.linspace(0,audio_time,num=len(signal)) #get the time

#plot the graph
plt.figure(1)
plt.title("Audio wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(time,signal)
plt.xlim(0,audio_time)
plt.show() #show the graph

