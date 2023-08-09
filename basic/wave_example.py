#audio file format 
#mp3
#flac
#wav

import wave

#audio signal 
#mono
#stereo
#sampler width 
#sapmle rate/ frequency
#number of frames
#values of frames

#open the file
obj = wave.open('conference.wav','rb')

#printing the details of the file
print ("Number of channels",obj.getnchannels()) #number of chanels
print ("Sample width",obj.getsampwidth()) #number of widths
print ("Frame rate.",obj.getframerate()) #frame rate
print ("Number of frames",obj.getnframes()) #number of frameve
print ("Parameters",obj.getparams()) #all parameters


print("------------------")
audio_time = obj.getnframes() / float(obj.getframerate()) #total time of audio
print ("Audio time",audio_time)

print("------------------")
#reading the number of frames of both channels
frame = obj.readframes(-1) #read frames
print (type(frame)) #type of frame
print (type(frame[0])) #frame value
print (len(frame)) #frame value

#closing the file
obj.close()


#saving the file
obj_new = wave.open('conference_new.wav','wb') #open new file
#setting the parameters of the file
obj_new.setnchannels(1) #set channels
obj_new.setsampwidth(2) #set channels
obj_new.setframerate(48000) #set frame rate


obj_new.writeframes(frame) #write frames

obj_new.close() #close the file

print("------------------")
print ("File saved")
