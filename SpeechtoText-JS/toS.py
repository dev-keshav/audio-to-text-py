import pyttsx3
import speech_recognition as sr
import time
from tkinter import *
from threading import *
from datetime import date
import pyautogui
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
def threading():
        t1=Thread(target=startrec)
        t1.start()
def threading1():
        t2=Thread(target=resumerec)
        t2.start()
def endrec():
    # Holds down the alt key
    pyautogui.keyDown("shift")

    # Presses the tab key once 
    pyautogui.press("delete")
    pyautogui.keyUp("shift")  
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
button.grid(row = 2, column = 0)
changeOnHover(button,"gray","#212529")
    # End button
button = Button(root, text='End', width=15, command=endrec,font="Bold",foreground="white",bg="#212529")
button.grid(row = 3, column = 0)
changeOnHover(button,"gray","#212529")
    # Size of GUI
root.geometry("600x250")
    # function for inputing time
def Take_inputtime():
        Output.delete("1.0","end")
        global TIME
        TIME = inputtime.get("1.0", "end-1c")
        print("Recording time : ",TIME)
        global ti
        global s
        if (len(TIME)==0):
            Output.insert(END, 'You have not set recording time\n')
            engine.say("You have not set recording time")
            engine.runAndWait()
        elif(TIME[-1]=='1' or TIME[-1]=='2'or TIME[-1]=='3'or TIME[-1]=='4'or TIME[-1]=='5' or TIME[-1]=='6' or TIME[-1]=='7' or TIME[-1]=='8' or TIME[-1]=='9' or TIME[-1]=='0'):
            Output.insert(END, 'Recording time has been  set\n')
            engine.say("Recording time has been  set")
            engine.runAndWait()
            ti=TIME
        else:
            Output.insert(END, "Wrong time inputed\n")
            TIME=""
            engine.say("Wrong time inputed")
            engine.runAndWait()
        return TIME
    # function for inputing file
def Take_input():
        Output.delete("1.0","end")
        global INPUT
        INPUT = inputtxt.get("1.0", "end-1c")
        print("File name : ",INPUT)
        global filename
        if(len(INPUT)>0):
            Output.insert(END, 'Your file has been saved\n')
            engine.say("Your file has been saved")
            engine.runAndWait()
            filename=INPUT
            my_file = open(filename, "w+")
            notes="NOTES\n"
            my_file.write(notes.center(30))
        else:
            Output.insert(END, "Wrong format of file\n")
            engine.say("Wrong format of file")
            engine.runAndWait()
        return INPUT
    # changing background color of the tkinter
root.config(bg="gray19")
    # heading of file
labettxt = Label(text = "Write the file name",font="bold",fg="white",bg="#212529")
changetextOnHover(labettxt,"red","white")
    # display of date
labeldistime=Label(root,text=f"{today:%B %d, %Y}",font="bold",fg="white",bg="black")
changetextOnHover(labeldistime,"red","white")
    #display of day
labeldisday=Label(root,text=f"{today:%A}",font="bold",fg="white",bg="black")
changetextOnHover(labeldisday,"red","white")
    # file inputing
inputtxt = Text(root, height = 1,width = 15,bg = "white")
    # heading of time
labeltime = Label(text= "Write the time for recording",font="bold",fg="white",bg="#212529")
changetextOnHover(labeltime,"red","white")
    # time inputing
inputtime = Text(root, height = 1,width = 10,bg="white")
    # output box
Output = Text(root, height = 4,width = 25,bg = "black",fg="white")
    # Set time button
Displaytime = Button(root,width = 10,text ="Set Time",bg="#212529",fg="white",command = lambda:Take_inputtime())
changeOnHover(Displaytime,"gray","#212529")
    # Set file button
Displaytxt = Button(root,width = 10,text ="Save File",bg="#212529",fg="white",command = lambda:Take_input())
changeOnHover(Displaytxt,"gray","#212529")
    # giving positions to all buttons
labeldistime.grid(row=4,column=0)
labeldisday.grid(row=4,column=4)
labettxt.grid(row=0,column=3)
inputtxt.grid(row=1,column=3)
Displaytxt.grid(row=1,column=4)
labeltime.grid(row=2,column=3)
inputtime.grid(row=3,column=3)
Displaytime.grid(row=3,column=4)
Output.grid(row=4,column=3)
    # removing resizing of window
root.resizable(False, False)
    # Logo adding
p1 = PhotoImage(file = 'stotlogo.png')
root.iconphoto(False, p1)
mainloop()
    # Making program to wait for 1 second
time.sleep(1)
# if __name__ == "__main__":
#     maincode()