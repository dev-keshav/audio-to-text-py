from pkg_resources import FileMetadata
import pyttsx3
import speech_recognition as sr
import time
from tkinter import *
from threading import *
from datetime import date
import pyautogui
import random
# def maincode():
today = date.today()
print("Today's date:", today)
engine = pyttsx3.init()
A=False
EP=False
ti=15
TIME=""
INPUT=""
def increment():
        global A
        A=True
def endprogram():
        global EP
        EP=True
r = sr.Recognizer()
# print(r.list_microphone_names())
def threading():
        t1=Thread(target=startrec)
        
        t1.start()
def threading1():
        t2=Thread(target=resumerec)
        t2.start()
def endrec():
    # Holds down the alt key
    # pyautogui.keyDown("shift")

    # # Presses the tab key once 
    # pyautogui.press("delete")
    # pyautogui.keyUp("shift")  
    Output.delete("1.0","end")
    try:
        if (len(TIME)==0 or len(INPUT)==0):
            Output.insert(END, "You have not started the recording\n")
            engine.say("You have not started the recording")
            engine.runAndWait()
        else:
            print("Recording has been saved successfully")
            global ti
            ti=0
            engine.say("Your Recording has been saved successfully")
            engine.runAndWait()
            root.destroy()
    except:
        engine.say("You are pressing 2 buttons at a time")
        engine.runAndWait()
def pauserec():
    Output.delete("1.0","end")
    try:
        if (len(TIME)==0 or len(INPUT)==0):
            engine.say("You have not started the recording")
            engine.runAndWait()
        else:
            Output.insert(END, "You have paused the recording\n")
            engine.say("You have paused the recording")
            engine.runAndWait()
    except:
            engine.say("You are pressing 2 buttons at a time")
            engine.runAndWait()
def resumerec():
        Output.delete("1.0","end")
        try:
            if (len(TIME)==0 or len(INPUT)==0):
                engine.say("You have not started the recording")
                engine.runAndWait()
            else:
                with sr.Microphone() as source:
                    Output.insert(END, "You have resumed the recording\n")
                    engine.say("You have resumed the recording!")
                    r.pause_threshold=1
                    r.energy_threshold = 4000  
                    r.dynamic_energy_threshold = True
                    engine.runAndWait()
                    try:
                        increment()
                        audio_data = r.record(source, duration=int(ti))
                        text = r.recognize_google(audio_data,language='en')
                        my_file = open(filename, "a")
                        my_file.write(text)
                        my_file.write('\n')
                        my_file.close()
                        print(text)
                    except:
                        print("Converting...\n")
        except:
            engine.say("You are pressing 2 buttons at a time")
            engine.runAndWait()
def startrec():
    Take_input()
    Take_inputtime()
    my_file = open(filename, "a")
    my_file.write('NOTES\n')
    my_file.close()
    Output.delete("1.0","end")
    if (len(TIME)==0 or len(INPUT)==0):
        engine.say("Recording can not be started")
        engine.runAndWait()   
    elif(A):
        Output.insert(END, "You have already started the recording\n")
        engine.say("You have already started the recording")
        engine.runAndWait()
    else:
        Output.insert(END, "Your Recording has been started\n")
        engine.say("Your Recording has been started!")
        engine.runAndWait()
        print("Recognizing.....")
        try:
            
            with sr.Microphone(device_index=0) as source:
                r.pause_threshold=1
                r.energy_threshold = 4000  
                r.dynamic_energy_threshold = True
                increment()
                audio_data = r.record(source, duration=int(ti))
                text = r.recognize_google(audio_data,language='en')
                my_file = open(filename, "a")
                my_file.write(text)
                my_file.write('\n')
                my_file.close()
                print(text)
        except:
            print("Converting...\n")
root = Tk()
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
root.title("Text-Recording")
    # Start button
button = Button(root, text='Start', width=15, command=threading,font="Bold",foreground="white",bg="#212529")
button.grid(row = 0, column = 0)
changeOnHover(button,"gray","#212529")
    # Pause button
button = Button(root, text='Pause', width=15, command=pauserec,font="Bold",foreground="white",bg="#212529")
button.grid(row = 1, column = 0)
changeOnHover(button,"gray","#212529")
    # Resume button
button = Button(root, text='Resume', width=15, command=threading1,font="Bold",foreground="white",bg="#212529")
button.grid(row = 0, column = 3)
changeOnHover(button,"gray","#212529")
    # End button
button = Button(root, text='End', width=15, command=endrec,font="Bold",foreground="white",bg="#212529")
button.grid(row = 1, column = 3)
changeOnHover(button,"gray","#212529")
    # Size of GUI
root.geometry("660x160")
    # function for inputing time
def Take_inputtime():
        Output.delete("1.0","end")
        global TIME
        TIME = '10'
        print("Recording time : ",TIME)
        global ti
        ti=TIME
        
def Take_input():
        Output.delete("1.0","end")
        global INPUT
        num = random.randrange(1,1000000000000000000)
        a=(str)(num)
        INPUT = 'random'+a+'.txt'
        print("File name : ",INPUT)
        global filename
        filename=INPUT
        return INPUT
    # changing background color of the tkinter
root.config(bg="gray19")
    # heading of file

    # display of date
labeldistime=Label(root,text=f"{today:%B %d, %Y}",font="bold",fg="white",bg="black")
changetextOnHover(labeldistime,"red","white")
    #display of day
labeldisday=Label(root,text=f"{today:%A}",font="bold",fg="white",bg="black")
changetextOnHover(labeldisday,"red","white")

Output = Text(root, height = 4,width = 25,bg = "black",fg="white")

labeldistime.grid(row=1,column=2)
labeldisday.grid(row=2,column=2)

Output.grid(row=0,column=2)
root.resizable(False, False)
    # Logo adding
p1 = PhotoImage(file = 'stotlogo.png')
root.iconphoto(False, p1)
mainloop()
    # Making program to wait for 1 second
time.sleep(1)
# if __name__ == "__main__":
#     maincode()