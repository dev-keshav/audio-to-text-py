
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
from fpdf import FPDF
import pyautogui

import pathlib
from botocore.client import Config
import datetime
import boto3
import smtplib

import math
import string
import sys

  # Change background color on hovering

def read_file(filename):
	
	try:
		with open(filename, 'r') as f:
			data = f.read()
		return data
	
	except IOError:
		print("Error opening or reading input file: ", filename)
		sys.exit()

# splitting the text lines into words
# translation table is a global variable
# mapping upper case to lower case and
# punctuation to spaces
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	
# returns a list of the words
# in the file
def get_words_from_line_list(text):
	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list


# counts frequency of each word
# returns a dictionary which maps
# the words to their frequency.
def count_frequency(word_list):
	
	D = {}
	
	for new_word in word_list:
		
		if new_word in D:
			D[new_word] = D[new_word] + 1
			
		else:
			D[new_word] = 1
			
	return D

# returns dictionary of (word, frequency)
# pairs from the previous dictionary.
def word_frequencies_for_file(filename):
	
	line_list = read_file(filename)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_frequency(word_list)

	print("File", filename, ":", )
	# print(len(line_list), "lines, ", )
	print(len(word_list), "words, ", )
	# print(len(freq_mapping), "distinct words")

	return freq_mapping


# returns the dot product of two documents
def dotProduct(D1, D2):
	Sum = 0.0
	
	for key in D1:
		
		if key in D2:
			Sum += (D1[key] * D2[key])
			
	return Sum

# returns the angle in radians
# between document vectors
def vector_angle(D1, D2):
	numerator = dotProduct(D1, D2)
	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	
	return math.acos(numerator / denominator)


# filename_1 = sys.argv[1]
# filename_2 = sys.argv[2]
def documentSimilarity(filename_1):
	

    filename_2=input("Enter manually typed file name : ")
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    # print("cosine similarity is: ")
    print("cosine similarity is: is: % 0.6f (radians)"% distance)
	
# Driver code




# def jaccard(list1, list2):
#     intersection = len(list(set(list1).intersection(list2)))
#     union = (len(list1) + len(list2)) - intersection
#     print(float(intersection) / union)
#     return float(intersection) / union

# #find Jaccard Similarity between the two sets 
# jaccard('duplicate533373.txt', "duplicate650182.txt")





# def Jaccard_Similarity(doc1): 
    
    # doc2=input("Enter the mannualy typed file name: ")

    
    # # List the unique words in a document
    # words_doc1 = set(doc1.lower().split()) 
    # words_doc2 = set(doc2.lower().split())
    
    # # Find the intersection of words list of doc1 & doc2
    # intersection = words_doc1.intersection(words_doc2)

    # # Find the union of words list of doc1 & doc2
    # union = words_doc1.union(words_doc2)
        
    # # Calculate Jaccard similarity score 
    # # using length of intersection set divided by length of union set

    # return float(len(intersection)) / len(union)
    # with open(doc_1) as f:
    #     lines1 = f.readlines()

    # with open(doc_2) as f:
    #     lines2 = f.readlines()

    # doc_1 = lines1[1]
    # doc_2 = lines2[1]













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
    t1 = Thread(target=textconver)
    t1.start()


def threading1():
    t2 = Thread(target=callback)
    t2.start()

def screenshotthread():
    Output.configure(state='normal')
    Output.insert(END, 'Speak Take Screenshot')
    Output.configure(state='disabled')
    Output.configure(state='normal')
    Output.insert(END,'\nRecognising')
    Output.configure(state='disabled')
    engine.say('Speak take screenshot')
    engine.runAndWait()
    t3=Thread(target=screenshot)
    t3.start()
def extensionthread():
    t4=Thread(target=extension)
    t4.start()

def browseFiles():
    Output.configure(state='normal')
    # Output.delete("1.0","end")
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("all files", "*.*"), ("Text files", "*.txt*")))
    if (len(filename) == 0):
        pass
    else:
        label_file_explorer.configure(text="File Chosed")
        Output.configure(state='normal')
        Output.insert(END, f"File Opened : {filename}")
        Output.insert(END, "\nPress Convert to Text")
        Output.configure(state='disabled')
        engine.say('Press Convert to Text')
        engine.runAndWait()


def rename(file):
    os.startfile(f"{os.getcwd()}/{file}")


def audio_dur(file):
    with contextlib.closing(wave.open(file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return int(duration)


def convert_file_to_pdf(file):
    print("name of file id:",file)
    pdf = FPDF()
    pdf.add_page()
    num = random.randrange(1, 1000000)

    a = (str)(num)
    duplicatefilepdf = 'pdf_file'+a
    
    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial", "B", size=18)  # For title text
            pdf.cell(w=200, h=10, txt=text, ln=1, align="C")
        else:
            pdf.set_font("Arial", size=15)  # For paragraph text
            pdf.multi_cell(w=0, h=10, txt=text, align="L")
    pdf.output(f"{duplicatefilepdf}.pdf")
    return (f"{duplicatefilepdf}.pdf")
    # print("Successfully converted!")


def convert_file_to_word(file):
    from docx import Document
    import glob
    import os

    num = random.randrange(1, 1000000000000000000)
    rando = (str)(num)
    
    docfile = 'docfile'+rando
    print(docfile)
    doc = Document()

    # files = glob.glob("*.txt")
    # print(files)
    # file = input("Scrivi il nome del file senza .txt: ") + ".txt"

    with open(file, 'r', encoding='utf-8') as openfile:
        line = openfile.read()
        doc.add_paragraph(line)
        # doc.save(file + ".docx")
        doc.save(docfile + ".docx")

    # os.system(file + ".docx")
    # os.system(docfile + ".docx")
    return (docfile + ".docx")


def textconver():
    global formate_of_file
    formate_of_file=clicked.get()
    print(formate_of_file)

    # label.config( text = clicked.get() )
    global filename
    print(len(filename))
    # if no file-------------------------
    if (clicked.get() == 'CHOOSE FILE FORMAT'):
        Output.insert(END, 'Choose file format first')
        engine.say('Choose file format first')
        engine.runAndWait()
    else:
        if (len(filename) == 0):
            Output.configure(state='normal')
            # Output.delete("1.0","end")
            Output.insert(END, "\n")
            Output.insert(END, "Please choose file first")
            Output.configure(state='disabled')
            engine.say('Please choose file first')
            engine.runAndWait()
        # if file---------------------------------
        else:

            Output.configure(state='normal')
            # Output.delete("1.0","end")
            Output.insert(END, "\n")
            Output.insert(END, "Converting....Wait for while")
            print('Converting....Wait for while')
            Output.configure(state='disabled')
            engine.say('Converting, Wait for while')
            engine.runAndWait()
            # -----------Converting to wav format--------
            m4a_file = filename
            num = random.randrange(1, 1000000000000000000)
            rando = (str)(num)
            wav_filename = 'random'+rando+'.wav'
            loopexec = 0

            if (filename.endswith('.mp3')):
                subprocess.call(['ffmpeg', '-i', m4a_file, wav_filename])
                file_handle = wav_filename
                # duplicatefile=wav_filename
            elif (filename.endswith('.wav') or filename.endswith('.m4a')):
                track = AudioSegment.from_file(m4a_file,  format='m4a')
                file_handle = track.export(wav_filename, format='wav')
                # duplicatefile=track.export(wav_filename, format='wav')
            else:
                subprocess.call(['ffmpeg', '-i', m4a_file, wav_filename])
                file_handle = wav_filename
                # duplicatefile=wav_filename
            # ----------------------------------
            try:
                # main program----------------------------------------------------------------------------------------------
                chunk_length_ms = 20000
                seg_len = chunk_length_ms
                ans = audio_dur(file_handle)
                # print(ans)
                chunk_length_ms = chunk_length_ms/1000
                loopexec = int(ans/chunk_length_ms)
                # print(filename.endswith('.m4a'))
                # print(filename.endswith('.mp3'))
                # print(wa)
                # print(file_handle)
                audio_file = AudioSegment.from_file(file_handle, "wav")
                # print(audio_file)
                chunks = make_chunks(audio_file, seg_len)
                # 'random2.txt' = 'random2.txt'
                # print('chlo')
                with open('random2.txt', mode="a") as file:
                    file.write("Recognized text:")
                    file.write("\n")

                with open('random2.txt', 'r+') as f:
                    f.truncate(0)
                    LiveOutput.configure(state='normal')
                    LiveOutput.delete("1.0", "end")
                    LiveOutput.configure(state='disabled')
                with open('random2.txt', mode="a") as file:
                    file.write("Recognized text:")
                    file.write("\n")
                    LiveOutput.configure(state='normal')
                    LiveOutput.insert(END, "Recognized text:\n")
                    LiveOutput.configure(state='disabled')
                # ans=audio_dur(filename)
                # global recognised
                global cnt
                cnt = 0
                # recognised=0
                for i, chunk in enumerate(chunks):
                    chunk_name = "{0}.wav".format(i)
                    # print("exporting", chunk_name)
                    chunk.export(chunk_name, format="wav")
                    file_handle = "{0}.wav".format(i)
                    audio_file = sr.AudioFile(file_handle)
                    if (loopexec == 0 or i == loopexec):
                        # print('over')
                        break
                    # print(i)
                    with audio_file as source:
                        try:
                            r.adjust_for_ambient_noise(source)
                            r.pause_threshold = 20
                            audio = r.record(source)
                            # print("Audio is",audio)
                            # print("Uper hai google ke")
                            try:

                                result = r.recognize_google(audio)
                                # recognised=1

                                # print("niche hai google ke")
                            except:
                                # recognised=0
                                cnt += 1

                                # if (cnt == 1):
                                    # Output.insert(
                                        # END, "Check Your Connection...")
                                    # engine.say("Check Your Connection!")

                            import time
                            import datetime
                            d = datetime.date.today()

                            t = time.strftime('%H:%M:%S')
                            print(result, end=' ')
                            num = random.randrange(1, 1000000)
                            a = (str)(num)
                        except:
                            print("we are in except block")
                            pass

                    with open('random2.txt', mode="a") as file:
                        try:
                            file.write(' ')
                            file.write(result)

                            LiveOutput.configure(state='normal')
                            LiveOutput.insert(END, f" {result}")
                            LiveOutput.configure(state='disabled')
                            # print("Conversion is completed and file is saved as ", 'random2.txt')
                            os.remove("{0}.wav".format(i))
                        except:
                            # print('ERROR')
                            if ("{0}.wav".format(i)):
                                os.remove("{0}.wav".format(i))
                            pass
                    # main program ends---------------------------------------------------------------------------------------
                # remaining program starts----------------------------------------------------------------------------------
                chunk_name = f"{loopexec}.wav"
                # print("exporting", chunk_name)
                chunk.export(chunk_name, format="wav")
                file_handle = f"{loopexec}.wav"
                audio_file = sr.AudioFile(file_handle)
                with audio_file as source:
                    try:
                        r.adjust_for_ambient_noise(source)
                        r.pause_threshold = 20
                        audio = r.record(source)
                        # print("Audio is",audio)
                        result = r.recognize_google(audio)
                        print(result, end=' ')
                        num = random.randrange(1, 1000000)
                        a = (str)(num)
                    except:
                        # print('Error')
                        pass
    # -----------------------------------

                        # overwrite file-------------------
                    num = random.randrange(1, 1000000)
                    a = (str)(num)
                    duplicatefile = 'duplicate'+a+'.txt'
                    with open('random2.txt', mode="a") as file:
                        # print(loopexec)
                        try:
                            file.write(' ')
                            file.write(result)
                            LiveOutput.configure(state='normal')
                            LiveOutput.insert(END, f" {result}")
                            LiveOutput.configure(state='disabled')
                            print(
                                "\nConversion is completed and file is saved as ", duplicatefile)
                            # os.remove(f"{os.getcwd()}/12.wav")
                            # os.remove("{0}.wav".format(loopexec))

                            # os.remove("{0}.wav".format(loopexec))
                            Output.configure(state='normal')
                            # Output.delete("1.0","end")
                            Output.insert(END, "\n")
                            Output.insert(
                                END, f"Conversion is completed and file is saved as {duplicatefile}")
                            Output.configure(state='disabled')
                            label_file_explorer.configure(
                                text="File is Opened")
                            engine.say(
                                'Conversion is completed, File is opening')
                            engine.runAndWait()
                        except:
                            pass
                # remaining program ends----------------------------------------------------------------------------------

                # duplicate file----------------
                if (1):
                    with open('random2.txt', 'r') as firstfile, open(duplicatefile, 'a') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)
                    # if(1):
                        # rename(duplicatefile)
                else:
                    pass

    # ==========================================AWS=============================================================

                # ================= AWS uploding file============

                try:
                    global formated_file
                    # print('login k upper')

                    s3 = boto3.resource(
                    's3',
                    
                    aws_access_key_id='AKIAWHVMGRIUPPGB2B5D',
                    aws_secret_access_key='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',
                    region_name="us-east-2",
                    
                    )
                    # print('login k niche')

                    if(formate_of_file == '.pdf'):
                        pdf_file= open('random2.txt', 'r')

                        formated_file=convert_file_to_pdf(pdf_file)
                        print(formated_file)
                        s3.meta.client.upload_file(formated_file,'sih-bugaches-22',f'Text:{d}{t}.pdf')
                    
                        # print('Nivhe hai upload')
                        c=f'Text:{d}{t}.pdf'
                        Output.configure(state='normal')
                        Output.insert(END,'\nWait, Uploading to AWS.....')
                        Output.configure(state='disabled')
                        # print('uploaded')
                
            #========================AWS Link Generate==============
                        
                        s3 = boto3.resource( 
                            "s3",
                            aws_access_key_id='AKIAWHVMGRIUPPGB2B5D', 
                            aws_secret_access_key='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',
                            region_name="us-east-2",)
                        url='https://sih-bugaches-22.s3.us-east-2.amazonaws.com/'+c

                    elif(formate_of_file == '.docx'):
                        # pdf_file= open('random2.txt', 'r')

                        formated_file=convert_file_to_word('random2.txt')
                        print(formated_file)
                        s3.meta.client.upload_file(formated_file,'sih-bugaches-22',f'Text:{d}{t}.docx')
                    
                        # print('Nivhe hai upload')
                        c=f'Text:{d}{t}.docx'
                        Output.configure(state='normal')
                        Output.insert(END,'\nWait, Uploading to AWS.....')
                        Output.configure(state='disabled')
                    
                        # print('uploaded')

                    
                
            #========================AWS Link Generate==============
                        
                        s3 = boto3.resource( 
                        "s3",
                        aws_access_key_id='AKIAWHVMGRIUPPGB2B5D', 
                        aws_secret_access_key='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',
                        region_name="us-east-2",)
                        url='https://sih-bugaches-22.s3.us-east-2.amazonaws.com/'+c

                    else:



                        s3.meta.client.upload_file('random2.txt','sih-bugaches-22',f'Text:{d}{t}.txt')
                    
                        print('Nivhe hai upload')
                        c=f'Text:{d}{t}.txt'
                        Output.configure(state='normal')
                        Output.insert(END,'\nWait, Uploading to AWS.....')
                        Output.configure(state='disabled')
                        print('uploaded')
                
            #========================AWS Link Generate==============
                        
                        s3 = boto3.resource( 
                            "s3",
                            aws_access_key_id='AKIAWHVMGRIUPPGB2B5D', 
                            aws_secret_access_key='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',
                            region_name="us-east-2",)
                        url='https://sih-bugaches-22.s3.us-east-2.amazonaws.com/'+c


            
                    
        #             s3.meta.client.upload_file('random2.txt','sih-bugaches',f'Text:{d}{t}.txt')
                    
        #             # print('Nivhe hai upload')
        #             c=f'Text:{d}{t}.txt'
        #             Output.configure(state='normal')
        #             Output.insert(END,'\nWait, Uploading to AWS.....')
        #             Output.configure(state='disabled')
        #             # print('uploaded')
            
        # #========================AWS Link Generate==============
                    
        #             s3 = boto3.resource( 
        #                 "s3",
        #                 aws_access_key_id='AKIASYJ7S6WKPKUE5VFO', 
        #                 aws_secret_access_key='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',
        #                 region_name="us-east-2",)
        #             url='https://sih-bugaches.s3.us-east-2.amazonaws.com/'+c
                        
                except:
                    

                    Output.insert(END, 'Unable to upload file')
                    engine.say('Unable to upload file')
                    engine.runAndWait()

               
                # ======================SEND MAIL===========================
                import smtplib
                try:
                    emailpassword = ' ashirbad@2389 '
                    emailsend = ' 2002389.cse.cec@cgc.edu.in '  # Space should be before and after the ''
                    if (1):
                        # print(clicked.get())
                        # print(clicked.get()=='.pdf')
                        global pdff
                        pdff = 0
                        if(clicked.get() == '.pdf'):
                            # convert_file_to_pdf(pdf_file)
                            pdf_file.close()
                            
                            # os.remove(f'{duplicatefile}.txt')
                        elif(clicked.get() == '.docx'):
                            # convert_file_to_word('random2.txt')
                            # os.remove(f'{duplicatefile}.txt')
                            # pdf_file.close()
                            pass
                        else:
                            pdff = 1
                            rename(duplicatefile)

                    else:
                        pass

                    if(len(emaillist) == 0):
                        Output.configure(state='normal')
                        Output.insert(END, "\n")
                        Output.insert(END, "You haven't add email")
                        Output.configure(state='disabled')
                        engine.say("You haven't add email")
                        engine.runAndWait()
                    else:
                        for e in emaillist:

                            emailreceive = [f' {e} ']
                            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                            type(smtpObj)
                            smtpObj.ehlo()
                            smtpObj.starttls()
  
                            smtpObj.login(
                                ' 2002389.cse.cec@cgc.edu.in ', emailpassword)
                            subject = 'BUG ACHES'
                            body = 'Download your Text file by the link:\n'+url
                            msg = f'Subject: {subject}\n\n{body}'
                            smtpObj.sendmail(emailsend, emailreceive, msg)
                            # print('Mail sent to: ',e)
                            Output.configure(state='normal')
                            Output.insert(END, "\n")
                            Output.insert(END, f"Mail sent to: {e}")
                            Output.insert(
                                END, "\nNow You can choose another file")
                            Output.configure(state='disabled')
                            engine.say(
                                'Mail send successfully, Now You can choose another file')
                            engine.runAndWait()
                            smtpObj.quit()
                except:
                    Output.insert(END, "Mail not send")
                    engine.say("Mail not send")
                    engine.runAndWait()
                
                

    # =========================================END_AWS=======================================================================
            except:
                Output.configure(state='normal')
                # Output.delete("1.0","end")
                Output.insert(
                    END, f"\nYou have choosen a wrong file :{filename}")
                Output.configure(state='disabled')
                engine.say('You have chosen wrong file')
                engine.runAndWait()
            
        if ("{0}.wav".format(loopexec)):
            os.remove("{0}.wav".format(loopexec))
        if ("{0}".format(wav_filename)):
            os.remove("{0}".format(wav_filename))
        file1.close()
        os.remove("random2.txt")
        if(pdff == 0):
            pass
            # os.remove(duplicatefile)
        # ------------------------------------------------------------------------ekgjaeiorgjaeriojioarjfiod
        clicked.set("CHOOSE FILE FORMAT")
        label_file_explorer.configure(text="No file Chosen")
        
    documentSimilarity('softtrans.txt')
    
    

    with open('manualtrans.txt') as f:
        lines1 = f.readlines()

    with open(duplicatefile) as f:
        lines2 = f.readlines()

    doc_1 = lines1[1]
    doc_2 = lines2[1]
        # List the unique words in a document
    words_doc1 = set(doc_1.lower().split()) 
    words_doc2 = set(doc_2.lower().split())
        
        # Find the intersection of words list of doc1 & doc2
    intersection = words_doc1.intersection(words_doc2)

        # Find the union of words list of doc1 & doc2
    union = words_doc1.union(words_doc2)
            
        # Calculate Jaccard similarity score 
        # using length of intersection set divided by length of union set
    a= float(len(intersection)) / len(union)

    with open('manualtrans.txt') as f:
        lines1 = f.readlines()

    with open(duplicatefile) as f:
        lines2 = f.readlines()

    doc_1 = lines1[1]
    doc_2 = lines2[1]

    # a=Jaccard_Similarity(doc_1,doc_2)
    print("jacard fille is:" ,a)



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
    j = 0
    while 1:
        if(j == 4):
            break
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        print(j)
        j = j+1

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
    link = 'https://live-voice2text.netlify.app/'
    Output.configure(state='normal')
    # Output.delete("1.0","end")
    Output.insert(END, "\nYou have clicked on the Live Recording")
    Output.configure(state='disabled')
    engine.say("Opening Live Recording")
    engine.runAndWait()
    webbrowser.open_new_tab(link)
    global query
    # screenshot()


def check(email):
    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        Output.insert(END, "Email Already added")
        return 1

    else:
        return 0


def addemail():
    email = emailbox.get(1.0, "end-1c")
    if email in emaillist:
        # print('Email Already added')
        Output.configure(state='normal')
        # Output.delete("1.0","end")
        Output.insert(END, "\n")
        Output.configure(state='disabled')
        engine.say('Email Already added')
        engine.runAndWait()
    elif (check(email)):
        emaillist.append(email)
        # print('Email added successfully')
        emailbox.delete("1.0", "end")
        emailbox.insert(END, '@gmail.com')
        # print(emaillist)

        Output.configure(state='normal')
        # Output.delete("1.0","end")
        Output.insert(END, "\n")
        Output.insert(END, "Email added successfully")
        Output.insert(END, "\n")
        Output.insert(END, f"Added Emails are:{emaillist}")
        Output.configure(state='disabled')
        engine.say('Email added successfully')
        engine.runAndWait()

    else:
        # print('Enter valid email')
        Output.configure(state='normal')
        # Output.delete("1.0","end")
        Output.insert(END, "\n")
        Output.insert(END, "Enter valid email")
        Output.configure(state='disabled')
        engine.say('Enter valid email')
        engine.runAndWait()

def takecommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")   
        # listen for 5 seconds and create the ambient noise energy level   
        r.adjust_for_ambient_noise(source, duration=1)  
        r.dynamic_energy_threshold = True 
        audio = r.listen(source) 




    try:
            # Output.configure(state='normal')
            # Output.insert(END,'\nRecognising')
            # Output.configure(state='disabled')
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            Output.configure(state='normal')
            # Output.insert(END,f"\nUser said: {query}")
            Output.configure(state='disabled')
            print(f"User Said: {query}\n")
            return query

    except Exception as e:
       # print(e)
        pass
        



    return query
def ssstop():
    global sih
    sih=1

def screenshot():
    # global sih
    global query
    sih=0
    # while(1):
        # print(sih)
        # if(sih):
        #     break
    query = takecommand().lower()
    if 'screenshot' in query:
                Output.configure(state='normal')
                Output.insert(END,'\ntell me the name of file')
                Output.configure(state='disabled')
                engine.say("tell me the name of file")
                engine.runAndWait()
                cm = takecommand().lower()
                Output.configure(state='normal')
                # Output.insert(END,'\ntaking screenshot')
                Output.configure(state='disabled')
                engine.say("taking screen shot")
                engine.runAndWait()
                img = pyautogui.screenshot()
                img.save(f"{cm}.png")
                Output.configure(state='normal')
                Output.insert(END,'\nScreenshot Saved')
                Output.configure(state='disabled')
                print('completed')
                engine.say("screenshot saved")
                engine.runAndWait()
    else:
        screenshot()
def extension():
    link = 'https://drive.google.com/drive/folders/1mlwi7oNFY7U_PvfbKufocQOTlI8427DO'
    Output.configure(state='normal')
    # Output.delete("1.0","end")
    Output.insert(END, "\nopening link of Chrome Extension")
    Output.configure(state='disabled')
    engine.say("opening link of Chrome Extension")
    engine.runAndWait()
    webbrowser.open_new_tab(link)
    global query

if __name__ == "__main__":

    global query
    global sih
    file1 = open("random2.txt", "w")
    loopexec = 1
    print("Current working directory: {0}".format(os.getcwd()))
    emaillist = []
    engine = pyttsx3.init()
    r = sr.Recognizer()
    # screenshot()
    today = date.today()
    root = Tk()
    root.title("Text-Recording")
    filename = ''
    # -------------------tkinter buttons------------------------------
    label_file_explorer = Label(root, text = "No file Chosen", width = 40, height = 1, fg = "blue")
    label_file_explorer.grid(row=3, column = 0)
    # label_file_explorer.place(x=20,y=705)
    button_explore = Button(root, text = "Browse File", command = browseFiles,width=15, font="Bold",foreground="white",bg="#212529")
    button_explore.grid(row=4, column=0)
    # button_explore.place(x=460,y=700)
    changeOnHover(button_explore, "gray", "#212529")
    button = Button(root, text='Convert and Download', width=20, font="Bold", foreground="white", bg="#212529",command=threading)
    changeOnHover(button, "gray", "#212529")
    button.grid(row=1, column = 1)
    # button.place(x=780,y=670)

    Output = Text(root, height = 30, width = 60, bg = "black",fg="white")
    Output.grid(row=0, column=0)
    Output.configure(state='disabled')
    LiveOutput = Text(root, height=30,width=60,bg = "black",fg="white")
    LiveOutput.grid(row=0, column=2)
    # LiveOutput.place(x=720,y=0)
    LiveOutput.configure(state='disabled')
    button = Button(root, text='Do Live Recording', width=15, height=1, font="Bold", foreground="white",bg="Red",command=threading1)
    changeOnHover(button, "gray", "red")
    button.grid(row=2, column = 2)
    # button.place(x=1100,y=670)
    # --------------------
    button = Button(root, text='Add Email', width=15 , font="Bold", foreground="white",bg="#212529",command=addemail)
    changeOnHover(button, "gray", "#212529")
    button.grid(row=2, column = 0)
    # button.place(x=460,y=642)
    emailbox = Text(root, height=1.5, width = 40,bg = "white",fg="black")
    emailbox.insert(END, '@gmail.com')
    emailbox.grid(row=1, column=0)

    # emailbox.place(x=10,y=640)
    # changetextOnHover(button,"red","white")

# Dropdown menu options
    options = [
        ".pdf",
        ".docx",
        ".txt"
    ]

# datatype of menu text
    clicked = StringVar()

# initial menu text
    clicked.set("CHOOSE FILE FORMAT")

# Create Dropdown menu
    drop = OptionMenu(root, clicked , *options )
    # drop.pack()
    drop.grid(row=2, column=1)
    # clicked = StringVar()
    # print(clicked.get(), ' text')
    # print("user ye selct kiya",clicked.get())
    labeldistime = Label(root, text=f"{today:%B %d, %Y}",font="bold",fg="white",bg="black")
    labeldisday = Label(root, text=f"{today:%A}",font="bold",fg="white",bg="black")
    # labeldistime.grid(row=1,column=2)
    # labeldistime.place(x=900,y=715)
    # labeldisday.grid(row=2,column=2)
    # labeldisday.place(x=1070,y=715)
    changetextOnHover(labeldisday, "red", "white")
    changetextOnHover(labeldistime, "red", "white")
    ssstart = Button(root, text='Take ScreenShot', width=15, height=1, font="Bold", foreground="white",bg="#212529",command=screenshotthread)
    changeOnHover(ssstart, "gray", "#212529")
    ssstart.grid(row=3, column = 2)
    downext = Button(root, text='Download extension', width=20, height=1, font="Bold", foreground="white",bg="#212529",command=extensionthread)
    changeOnHover(downext, "gray", "#212529")
    downext.grid(row=4, column = 2)
    # sstop = Button(root, text='Stop ScreenShot', width=15, height=1, font="Bold", foreground="white",bg="#212529",command=ssstop)
    # changeOnHover(sstop, "gray", "#212529")
    # sstop.grid(row=4, column = 2)
    
    # ------------------------------------------------------------
    root.configure(bg='gray19')
    # p1 = PhotoImage(file = 'stotlogo.png')
    # root.iconphoto(False, p1)
    root.resizable(False, False)
    # root.geometry('1385x750')
    # os.chdir('C:/Users/hp/Downloads')
    # print("Current working directory: {0}".format(os.getcwd()))
    mainloop()