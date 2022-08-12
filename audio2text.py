import speech_recognition as sr
import boto3
import speech_recognition as sr
import os
import datetime
r = sr.Recognizer()

audio_file = sr.AudioFile("harsh.wav")

with audio_file as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)
result = r.recognize_google(audio)

with open("harsh.txt",mode ="w") as file:
     file.write("Recognized text:")
     file.write("\n")
     file.write(result)
     print("Hurray! conversion is completed")



r = sr.Recognizer()

audio_file = sr.AudioFile("download.wav")

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
result = r.recognize_google(audio)

with open("test.txt",mode ="w") as file:
    file.write("Recognized text:")
    file.write("\n")
    file.write(result)
    print("Hurray! conversion is completed")

#====== make file unique
now = datetime.datetime.now()
fileun=str(now)

#=======fretching the test file 


file_loc=os.path.abspath('test.txt') 
print(file_loc)

#========== AWS uploding file
client = boto3.client(
    's3',
    aws_access_key_id='AKIA6LMBN6TNRNNGBNI5',  
    aws_secret_access_key='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',
    
)


s3=boto3.resource('s3')
s3.meta.client.upload_file('file_loc','newup1319',fileun)    #newup1319 is the bucket name , file_loc is the file to send ,fileun will be show on object
