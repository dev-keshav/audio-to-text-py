import speech_recognition as sr
from pydub.utils import make_chunks
import pyaudio
import wave
from tkinter import *
from threading import Thread
from pydub import AudioSegment
from tkinter import filedialog
from datetime import date
import webbrowser
import random
import subprocess
import pyttsx3
import os
import wave
import contextlib
import re



    # Change background color on hovering
def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
    # Change text color on hovering
def changetextOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            fg=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            fg=colorOnLeave))
def threading():
        t1=Thread(target=textconver)
        t1.start()  
def threading1():
    t2=Thread(target=callback)
    t2.start()
def browseFiles():
    Output.configure(state='normal')
    Output.delete("1.0","end")
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    if(len(filename)==0):
        pass
    else:
        label_file_explorer.configure(text="File Chosed")
        Output.configure(state='normal')
        Output.insert(END, f"File Opened : {filename}")
        Output.insert(END,"\nPress Convert to Text")
        Output.configure(state='disabled')
        engine.say('Press Convert to Text')
        engine.runAndWait()
def rename(file):
    os.startfile(f"{os.getcwd()}/{file}")
def audio_dur(file):
    with contextlib.closing(wave.open(file,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return int(duration)
def textconver():
    
    global filename
    print(len(filename))
    if(len(filename)==0):
        Output.configure(state='normal')
        Output.delete("1.0","end")
        Output.insert(END, "Please choose file first")
        Output.configure(state='disabled')
        engine.say('Please choose file first')
        engine.runAndWait()
    else:
        
        Output.configure(state='normal')
        Output.delete("1.0","end")
        Output.insert(END, "Converting....Wait for while")
        print('Converting....Wait for while')
        Output.configure(state='disabled')
        engine.say('Converting, Wait for while')
        engine.runAndWait()
        # -----------Converting to wav format--------
        m4a_file = filename
        num = random.randrange(1,1000000000000000000)
        rando=(str)(num)
        wav_filename = 'random'+rando+'.wav'
        loopexec=0
        # print(filename.endswith('.m4a'))
        # print(filename.endswith('.mp3'))
        
        # if(filename.endswith('.m4a')):
        #     print('hi')
        #     track = AudioSegment.from_file(m4a_file,  format= 'm4a')
        #     print('come')
        #     file_handle = track.export(wav_filename, format='wav')
        #     print('here')
        #     # duplicatefile=track.export(wav_filename, format='wav')
        if(filename.endswith('.mp3')):
            subprocess.call(['ffmpeg', '-i', m4a_file,wav_filename])
            file_handle=wav_filename
            # duplicatefile=wav_filename
        elif(filename.endswith('.wav') or filename.endswith('.m4a')):
            track = AudioSegment.from_file(m4a_file,  format= 'm4a')
            file_handle = track.export(wav_filename, format='wav')
            # duplicatefile=track.export(wav_filename, format='wav')
        else:
            subprocess.call(['ffmpeg', '-i', m4a_file,wav_filename])
            file_handle=wav_filename
            # duplicatefile=wav_filename
        # ----------------------------------
        try:
            # main program----------------------------------------------------------------------------------------------
            chunk_length_ms = 20000
            seg_len=chunk_length_ms
            ans=audio_dur(file_handle)
            # print(ans)
            chunk_length_ms=chunk_length_ms/1000
            loopexec=int(ans/chunk_length_ms)
            # print(filename.endswith('.m4a'))
            # print(filename.endswith('.mp3'))
            # print(wa)
            # print(file_handle)
            audio_file = AudioSegment.from_file(file_handle, "wav")
            # print(audio_file)
            chunks = make_chunks(audio_file, seg_len)
            INPUT = 'random2.txt'
            # print('chlo')
            with open(INPUT, mode="a") as file:
                file.write("Recognized text:")
                file.write("\n")
            with open(INPUT, 'r+') as f:
                f.truncate(0)
            with open(INPUT, mode="a") as file:
                file.write("Recognized text:")
                file.write("\n")
            # ans=audio_dur(filename)
            for i, chunk in enumerate(chunks):
                chunk_name = "{0}.wav".format(i)
                # print("exporting", chunk_name)
                chunk.export(chunk_name, format="wav")
                file_handle = "{0}.wav".format(i)
                audio_file = sr.AudioFile(file_handle)
                if(loopexec==0 or i==loopexec):
                    # print('over')
                    break
                # print(i)
                with audio_file as source:
                    try:
                        r.adjust_for_ambient_noise(source)
                        r.pause_threshold=20
                        audio = r.record(source)
                        # print("Audio is",audio)
                        result = r.recognize_google(audio)
                        print(result,end=' ')
                        num = random.randrange(1, 1000000)
                        a = (str)(num)
                    except:
                        pass
                        # print('Error')
                with open(INPUT, mode="a") as file:
                    try:
                        file.write(' ')
                        file.write(result)
                        # print("Conversion is completed and file is saved as ", INPUT)
                        os.remove("{0}.wav".format(i))
                    except:
                        # print('ERROR')
                        if("{0}.wav".format(i)):
                            os.remove("{0}.wav".format(i))
                        pass
                # main program ends---------------------------------------------------------------------------------------
            # remaining program starts----------------------------------------------------------------------------------
            chunk_name = f"{loopexec}.wav"
            # print("exporting", chunk_name)
            chunk.export(chunk_name, format="wav")
            file_handle =f"{loopexec}.wav"
            audio_file = sr.AudioFile(file_handle)
            with audio_file as source:
                try:
                    r.adjust_for_ambient_noise(source)
                    r.pause_threshold=20
                    audio = r.record(source)
                    # print("Audio is",audio)
                    result = r.recognize_google(audio)
                    print(result,end=' ')
                    num = random.randrange(1, 1000000)
                    a = (str)(num)
                except:
                    # print('Error')
                    pass
# -----------------------------------

                    # overwrite file-------------------
                num = random.randrange(1,1000000)
                a=(str)(num)
                duplicatefile='duplicate'+a+'.txt'
                with open(INPUT, mode="a") as file:
                    print(loopexec)
                    try:
                        file.write(' ')
                        file.write(result)
                        print("\nConversion is completed and file is saved as ", duplicatefile)
                        # os.remove(f"{os.getcwd()}/12.wav")
                        # os.remove("{0}.wav".format(loopexec))

                        # os.remove("{0}.wav".format(loopexec))
                        Output.configure(state='normal')
                        Output.delete("1.0","end")
                        Output.insert(END, f"Conversion is completed and file is saved as {duplicatefile}")
                        Output.configure(state='disabled')
                        label_file_explorer.configure(text="File is Opened")
                        engine.say('Conversion is completed, File is opening, You can rename you saved file')
                        engine.runAndWait()
                    except:
                        print('ERROR')
                        # os.remove("{0}.wav".format(loopexec))
                        pass
            # remaining program ends----------------------------------------------------------------------------------

            # duplicate file----------------
            with open(INPUT,'r') as firstfile, open(duplicatefile,'a') as secondfile:
                for line in firstfile:
                    secondfile.write(line)
            rename(duplicatefile)
        except :
            Output.configure(state='normal')
            Output.delete("1.0","end")
            Output.insert(END, f"You have choosen a wrong file :{filename}")
            Output.configure(state='disabled')
            engine.say('You have chosen wrong file')
            engine.runAndWait()
    if("{0}.wav".format(loopexec)):
        os.remove("{0}.wav".format(loopexec))
    if("{0}".format(wav_filename)):
        os.remove("{0}".format(wav_filename))
def voicerec():
    
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    j=0
    while 1:
        if(j==4):
            break
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        print(j)
        j=j+1

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
def callback():
    link='https://speechtotex.netlify.app/'
    Output.configure(state='normal')
    Output.delete("1.0","end")
    Output.insert(END,f"You have clicked on the Live Recording")
    Output.configure(state='disabled')
    engine.say("Opening Live Recording")
    engine.runAndWait()
    webbrowser.open_new_tab(link)

def check(email):
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return 1
 
    else:
        return 0
def addemail():
    email = emailbox.get(1.0, "end-1c")
    if email in emaillist:
        print('Email Already added')
        Output.configure(state='normal')
        Output.delete("1.0","end")
        Output.insert(END, "Email Already added")
        Output.configure(state='disabled')
        engine.say('Email Already added')
        engine.runAndWait()
    elif(check(email)):
        emaillist.append(email)
        print('Email added successfully')
        emailbox.delete("1.0","end")
        print(emaillist)
        Output.configure(state='normal')
        Output.delete("1.0","end")
        Output.insert(END, "Email added successfully")
        Output.configure(state='disabled')
        engine.say('Email added successfully')
        engine.runAndWait()
    else:
        print('Enter valid email')
        Output.configure(state='normal')
        Output.delete("1.0","end")
        Output.insert(END, "Enter valid email")
        Output.configure(state='disabled')
        engine.say('Enter valid email')
        engine.runAndWait()


if __name__ == "__main__" :
    print("Current working directory: {0}".format(os.getcwd()))
    emaillist=[]
    engine = pyttsx3.init()
    r = sr.Recognizer()
    today = date.today()
    root = Tk()
    root.title("Text-Recording")
    filename =''
    # -------------------tkinter buttons------------------------------
    label_file_explorer = Label(root,text = "No file Chosen", width = 40, height = 1,fg = "blue")
    label_file_explorer.grid(row = 2, column = 0)
    button_explore = Button(root,text = "Browse File",command = browseFiles,width=15, font="Bold",foreground="white",bg="#212529")
    button_explore.grid(row=3, column=0)
    changeOnHover(button_explore,"gray","#212529")
    button = Button(root, text='Convert to text', width=15, font="Bold",foreground="white",bg="#212529",command=threading)
    changeOnHover(button,"gray","#212529")
    button.grid(row = 4, column = 0)
    Output = Text(root, height = 5,width = 40,bg = "black",fg="white")
    Output.grid(row=0,column=0)
    Output.configure(state='disabled')
    button = Button(root, text='Do Live Recording', width=15,height=2, font="Bold",foreground="white",bg="Red",command=threading1)
    changeOnHover(button,"gray","red")
    button.grid(row = 0, column = 2)
    button = Button(root, text='Add Email', width=15 ,font="Bold",foreground="white",bg="#212529",command=addemail)
    changeOnHover(button,"gray","#212529")
    button.grid(row = 1, column = 2)
    emailbox = Text(root,height=1,width = 40,bg = "white",fg="black")
    emailbox.insert(END,'@gmail.com')
    emailbox.grid(row=1,column=0)
    # changetextOnHover(button,"red","white")
    
    labeldistime=Label(root,text=f"{today:%B %d, %Y}",font="bold",fg="white",bg="black")
    labeldisday=Label(root,text=f"{today:%A}",font="bold",fg="white",bg="black")
    labeldistime.grid(row=2,column=2)
    labeldisday.grid(row=3,column=2)
    changetextOnHover(labeldisday,"red","white")
    changetextOnHover(labeldistime,"red","white")
    # ------------------------------------------------------------
    root.configure(bg='gray19')
    p1 = PhotoImage(file = 'stotlogo.png')
    root.iconphoto(False, p1)
    root.resizable(False, False)
    # os.chdir('C:/Users/hp/Downloads')
    # print("Current working directory: {0}".format(os.getcwd()))
    mainloop()