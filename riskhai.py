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
from gtts import gTTS


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
# def get_words_from_line_list(text):
	
# 	text = text.translate(translation_table)
# 	word_list = text.split()
	
# 	return word_list


# # counts frequency of each word
# # returns a dictionary which maps
# # the words to their frequency.
# def count_frequency(word_list):
	
# 	D = {}
	
# 	for new_word in word_list:
		
# 		if new_word in D:
# 			D[new_word] = D[new_word] + 1
			
# 		else:
# 			D[new_word] = 1
			
# 	return D

# # returns dictionary of (word, frequency)
# # pairs from the previous dictionary.
# def word_frequencies_for_file(filename):
	
# 	line_list = read_file(filename)
# 	word_list = get_words_from_line_list(line_list)
# 	freq_mapping = count_frequency(word_list)

# 	print("File", filename, ":", )
# 	# print(len(line_list), "lines, ", )
# 	print(len(word_list), "words, ", )
# 	# print(len(freq_mapping), "distinct words")

# 	return freq_mapping


# # returns the dot product of two documents
# def dotProduct(D1, D2):
# 	Sum = 0.0
	
# 	for key in D1:
		
# 		if key in D2:
# 			Sum += (D1[key] * D2[key])
			
# 	return Sum

# # returns the angle in radians
# # between document vectors
# def vector_angle(D1, D2):
# 	numerator = dotProduct(D1, D2)
# 	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	
# 	return math.acos(numerator / denominator)


# # filename_1 = sys.argv[1]
# # filename_2 = sys.argv[2]
# def documentSimilarity(filename_1):
	

#     filename_2=input("Enter manually typed file name : ")
#     sorted_word_list_1 = word_frequencies_for_file(filename_1)
#     sorted_word_list_2 = word_frequencies_for_file(filename_2)
#     distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
#     # print("cosine similarity is: ")
#     print("cosine similarity is: is: % 0.6f (radians)"% distance)
	
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
def threadingWithSum():
    to= Thread(target = texttoSummary)
    to.start()

    


def threading1():
    t2 = Thread(target=callback)
    t2.start()
def threadingfortext():
    too=Thread(target=textToSpeech)
    too.start()
def textToSpeech():
    global textfilename
    
    
    
    if (len(textfilename) == 0):
        Output.configure(state='normal')
        # Output.delete("1.0","end")
        Output.insert(END, "\n")
        Output.insert(END, "Please choose file first")
        Output.configure(state='disabled')
        engine.say('Please choose file first')
        engine.runAndWait()
    # if file---------------------------------
    elif (textfilename.endswith('.txt')==FALSE):
        Output.configure(state='normal')
        Output.insert(END,'\nYou have choosen wrong file, Choose text file only')
        Output.configure(state='disabled')
        engine.say('Choose text file only')
        engine.runAndWait()
        
    else:

        Output.configure(state='normal')
        # Output.delete("1.0","end")
        Output.insert(END, "\n")
        Output.insert(END, "Converting....Wait for while")
        print('Converting....Wait for while')
        Output.configure(state='disabled')
        engine.say('Converting, Wait for while')
        engine.runAndWait()
        print(textfilename)
        with open(textfilename) as f:
            lines=f.readlines()
        with open(f"{textfilename}", 'r') as fp:
            lines1 = len(fp.readlines())
        print('Total Number of lines:', lines)
        # print(lines[0])
        # print(lines[1])
        mytext=''
        for i in range(0,lines1):
            mytext += lines[i]
            print(mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        num = random.randrange(1, 1000000)
        a = (str)(num)
        audiofilename='audiofile'+a
        myobj.save(f"{audiofilename}.mp3")
        Output.configure(state='normal')
        Output.insert(END, "\n")
        Output.insert(END, f"conversion is completed. File is saved as {audiofilename}")
        Output.insert(END, f"\nYou can choose another file")
        # print('Converting....Wait for while')
        Output.configure(state='disabled')
        engine.say('conversion is completed.')
        engine.say('You can choose another file!')
        engine.runAndWait()
       




    # Import the required module for text
# to speech conversion
  
    

def screenshotthread():
    Output.configure(state='normal')
    Output.insert(END, '\nSpeak Take Screenshot')
    Output.configure(state='disabled')
    Output.configure(state='normal')
    Output.insert(END,'\nRecognising')
    Output.configure(state='disabled')
    engine.say('Speak take screenshot')
    engine.runAndWait()
    t3=Thread(target=screenshot)
    t3.start()

def browseFiles():
    Output.configure(state='normal')
    # Output.delete("1.0","end")
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("all files", "*.*"), ("Text files", "*.txt*")))
    if (len(filename) == 0):
        pass
    else:
        # label_file_explorer.configure(text="File Chosed")
        Output.configure(state='normal')
        Output.insert(END,"\n")
        Output.insert(END, f"File Opened : {filename}")
        Output.insert(END, "\nPress Convert to Text")
        Output.configure(state='disabled')
        engine.say('Press Convert to Text')
        engine.runAndWait()

def browseFilesfortext():
    Output.configure(state='normal')
    # Output.delete("1.0","end")
    global textfilename
    textfilename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("all files", "*.*"), ("Text files", "*.txt*")))
    if (len(textfilename) == 0):
        pass
    else:
        # label_file_explorer.configure(text="File Chosed")
        Output.configure(state='normal')
        Output.insert(END, f"File Opened : {textfilename}")
        Output.insert(END, "\nPress Convert to Audio")
        Output.configure(state='disabled')
        engine.say('Press Convert to Audio')
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
            generatedFile = 'recfile.wav'
            welcome  = AudioSegment.from_wav('silentvid.wav')
            thankyou = AudioSegment.from_wav(wav_filename)
            filenameswithbeep = [welcome]
            combined = AudioSegment.empty()
            filenameswithbeep.extend([thankyou])
            for fname in filenameswithbeep:
                combined += fname
            generatedFile=wav_filename
            combined.export(generatedFile, format="wav")

            # wav_filename=     
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
                global cnt
                cnt = 0
                # recognised=0
                # audio_file = sr.AudioFile('output.wav')
                # with audio_file as source:
                #     try:
                #         r.adjust_for_ambient_noise(source)
                #         r.pause_threshold = 20
                #         audio = r.record(source)
                #         # print("Audio is",audio)
                #         result = r.recognize_google(audio)
                #         print(result, end=' ')
                #         num = random.randrange(1, 1000000)
                #         a = (str)(num)
                #     except:
                #         # print('Error')
                #         pass
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
                            # label_file_explorer.configure(
                            #     text="File is Opened")
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
                print("**********************************************************************")
                
                try:
                    global formated_file
                    print('login k upper')

                    s3 = boto3.resource(
                    's3',
                    
                    aws_access_key_id='AKIAUBLVNIXIBAMOCV4A',
                    aws_secret_access_key='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',
                    region_name="ap-south-1",
                    
                    )
                    print('login k niche')
                    
                    
                    print("email list check")
                    if(formate_of_file == '.pdf'):
                        print("Under pdf")
                        pdf_file= open('random2.txt', 'r')

                        formated_file=convert_file_to_pdf(pdf_file)
                        print(formated_file)
                        if(len(emaillist)!=0):
                            
                            s3.meta.client.upload_file(formated_file,'anio0007',f'Text:{d}{t}.pdf')
                        
                            # print('Nivhe hai upload')
                            c=f'Text:{d}{t}.pdf'
                            Output.configure(state='normal')
                            Output.insert(END,'\nWait, Uploading to AWS.....')
                            Output.configure(state='disabled')
                            # print('uploaded')
                    
                #========================AWS Link Generate==============
                            
                            s3 = boto3.resource( 
                                "s3",
                                aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                                aws_secret_access_key='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',
                                region_name="ap-south-1",)
                            url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c

                    elif(formate_of_file == '.docx'):
                        # pdf_file= open('random2.txt', 'r')
                        print("Under docx")

                        formated_file=convert_file_to_word('random2.txt')
                        print(formated_file)
                        if(len(emaillist)!=0):
                            s3.meta.client.upload_file(formated_file,'anio0007',f'Text:{d}{t}.docx')
                    
                        # print('Nivhe hai upload')
                            c=f'Text:{d}{t}.docx'
                            Output.configure(state='normal')
                            Output.insert(END,'\nWait, Uploading to AWS.....')
                            Output.configure(state='disabled')
                        
                            # print('uploaded')

                        
                    
                #========================AWS Link Generate==============
                            
                            s3 = boto3.resource( 
                            "s3",
                            aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                            aws_secret_access_key='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',
                            region_name=" ap-south-1",)
                            url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c

                    else:

                        print("Under txt")
                        if(len(emaillist)!=0):
                            s3.meta.client.upload_file('random2.txt','anio0007',f'Text:{d}{t}.txt')
                        
                            c=f'Text:{d}{t}.txt'
                            Output.configure(state='normal')
                            Output.insert(END,'\nWait, Uploading to AWS.....')
                            Output.configure(state='disabled')
                            # print('uploaded')
                    
                #========================AWS Link Generate==============
                            
                            s3 = boto3.resource( 
                                "s3",
                                aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                                aws_secret_access_key='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',
                                region_name=" ap-south-1",)
                            url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c
                            


            
                    
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
        #                 region_name=" ap-south-1",)
        #             url='https://sih-bugaches.s3. ap-south-1.amazonaws.com/'+c
                        
                except:
                    

                    Output.insert(END, 'Unable to upload file')
                    engine.say('Unable to upload file')
                    engine.runAndWait()

               
                # ======================SEND MAIL===========================
                import smtplib
                try:
                    emailpassword = ' Iloveyouadi@143 '
                    emailsend = ' 2002807.it.cec@cgc.edu.in '  # Space should be before and after the ''
                    print("Login Of email")
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
                    print("Email len",len(emaillist))
                    if(len(emaillist) == 0):
                        Output.configure(state='normal')
                        Output.insert(END, "\n")
                        Output.insert(END, "You haven't add email")
                        Output.configure(state='disabled')
                        engine.say("You haven't add email")
                        engine.runAndWait()
                    else:
                        print("Login Of email ke niche elel")
                        for e in emaillist:

                            emailreceive = [f' {e} ']
                            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                            type(smtpObj)
                            smtpObj.ehlo()
                            smtpObj.starttls()
  
                            smtpObj.login(
                                ' 2002807.it.cec@cgc.edu.in ', emailpassword)
                            print("Login Of email  ke  ek aur")
                            subject = 'OPTIMAL TECHIES'
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
                                'Mail send successfully!')
                            engine.runAndWait()
                            smtpObj.quit()
                        engine.say(
                                'Now You can choose another file')
                        engine.runAndWait()
                        
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
        # label_file_explorer.configure(text="No file Chosen")
        



        # Accurracy testing------------------------------------------------------------------
    # documentSimilarity('softtrans.txt')
    
    

    # with open('manualtrans.txt') as f:
    #     lines1 = f.readlines()

    # with open(duplicatefile) as f:
    #     lines2 = f.readlines()

    # doc_1 = lines1[1]
    # doc_2 = lines2[1]
    # words_doc1 = set(doc_1.lower().split()) 
    # words_doc2 = set(doc_2.lower().split())
        
    # intersection = words_doc1.intersection(words_doc2)

    # union = words_doc1.union(words_doc2)
            
    # a= float(len(intersection)) / len(union)

    # with open('manualtrans.txt') as f:
    #     lines1 = f.readlines()

    # with open(duplicatefile) as f:
    #     lines2 = f.readlines()

    # doc_1 = lines1[1]
    # doc_2 = lines2[1]

    # print("jacard fille is:" ,a)
# ------------------------------------------------------------------------------------

def texttoSummary():

    
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
            generatedFile = 'recfile.wav'
            welcome  = AudioSegment.from_wav('silentvid.wav')
            thankyou = AudioSegment.from_wav(wav_filename)
            filenameswithbeep = [welcome]
            combined = AudioSegment.empty()
            filenameswithbeep.extend([thankyou])
            for fname in filenameswithbeep:
                combined += fname
            generatedFile=wav_filename
            combined.export(generatedFile, format="wav")

            # wav_filename=     
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
                global cnt
                cnt = 0
                # recognised=0
                # audio_file = sr.AudioFile('output.wav')
                # with audio_file as source:
                #     try:
                #         r.adjust_for_ambient_noise(source)
                #         r.pause_threshold = 20
                #         audio = r.record(source)
                #         # print("Audio is",audio)
                #         result = r.recognize_google(audio)
                #         print(result, end=' ')
                #         num = random.randrange(1, 1000000)
                #         a = (str)(num)
                #     except:
                #         # print('Error')
                #         pass
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
                            # label_file_explorer.configure(
                            #     text="File is Opened")
                            engine.say(
                                'Conversion is completed, File is opening')
                            engine.runAndWait()
                        except:
                            pass
                # remaining program ends----------------------------------------------------------------------------------
                # ******************************************Sumarize Code **********************************
                deb=1
                print("Summaray : 1")
                import spacy
                from spacy.lang.en.stop_words import STOP_WORDS

                from heapq import nlargest
                with open('random2.txt') as f:
                    lines = f.readlines()
                # print()
                print("Summaray : 2")
                text=lines[1]
                # print("Text hai\n")
                # print(text)
                if(len(text)>=3681):
                

                    print("Summaray : 3")
                    stopwords= list(STOP_WORDS)
                    print("Summaray : 4")
                    nlp=spacy.load('en_core_web_sm')
                    print("Summaray : 5")

                    doc=nlp(text)
                    print(doc)
                    print("Summaray : 6")

                    tokens= [token.text for token in doc]
                    print(tokens)
                    print("7")
                    # print(tokens)
                    from string import punctuation
                    punctuation=punctuation+ '/n'
                    print(punctuation)
                    print("8")
                    # print(punctuation)

                    word_freq={}
                    print(word_freq)
                    print("9")
                    for word in doc:
                        if word.text.lower() not in stopwords:
                            if word.text.lower() not in punctuation:
                                if word.text not in word_freq.keys():
                                    word_freq[word.text] = 1
                                else:
                                    word_freq[word.text] += 1
                    print(word_freq)
                    print("10")
                    max_freq = max(word_freq.values())
                    print(max_freq)
                    print("11")
                    for word in word_freq.keys():
                        word_freq[word] = word_freq[word]/max_freq

                    print(word_freq)
                    print("12")
                    sen_tokens= [sen for sen in doc.sents]
                    print(sen_tokens)

                    sen_scores = {}
                    print("13")
                    for sent in sen_tokens:
                        for word in sent:
                            if word.text.lower() in word_freq.keys():
                                if sent not in sen_scores.keys():
                                    sen_scores[sent]= word_freq[word.text.lower()]
                                else:
                                    sen_scores[sent] += word_freq[word.text.lower()]
                    print(sen_scores)

                    print(len(sen_tokens))
                    print("14")
                    select_length = int(len(sen_tokens)*0.4)
                    print((select_length))
                    print("15")
                    summary = nlargest(select_length, sen_scores , key=sen_scores.get)
                    print("Old Summar\n",summary)

                    final_summary = [word.text for word in summary]
                    summary = ' '.join(final_summary)
                    print("file ke upper")
                    with open('random2.txt','r+') as f:
                        f.truncate(0)
                            # print(loopexec)
                    print("file trunc ke bad ")
                    with open("random2.txt", 'a') as file:
                        try:
                            file.write(' ')
                            file.write(summary)
                        except:
                            pass
                    print("last file")

                    print(summary)
                    print("Length Of original file: ",len(text))
                    print("Length of summary: ",len(summary))
                else:
                    pass





                #********************************************Code End*****************************************
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
                    print('login k upper')

                    s3 = boto3.resource(
                    's3',
                    
                    aws_access_key_id='AKIAUBLVNIXIBAMOCV4A',
                    aws_secret_access_key='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',
                    region_name="ap-south-1",
                    
                    )
                    print('login k niche')
                    
                    # if(len(emaillist)!=0):
                    print("email list check")
                    print(emaillist)
                    if(formate_of_file == '.pdf'):
                        print("Under pdf")
                        pdf_file= open('random2.txt', 'r')

                        formated_file=convert_file_to_pdf(pdf_file)
                        print(formated_file)
                        print(emaillist)
                        if(len(emaillist)!=0):
                            s3.meta.client.upload_file(formated_file,'anio0007',f'Text:{d}{t}.pdf')
                    
                        # print('Nivhe hai upload')
                            c=f'Text:{d}{t}.pdf'
                            Output.configure(state='normal')
                            Output.insert(END,'\nWait, Uploading to AWS.....')
                            Output.configure(state='disabled')
                            # print('uploaded')
                    
                #========================AWS Link Generate==============
                            
                            s3 = boto3.resource( 
                                "s3",
                                aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                                aws_secret_access_key='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',
                                region_name="ap-south-1",)
                            url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c

                    elif(formate_of_file == '.docx'):
                        # pdf_file= open('random2.txt', 'r')
                        print("Under docx")

                        formated_file=convert_file_to_word('random2.txt')
                        print(formated_file)
                        s3.meta.client.upload_file(formated_file,'anio0007',f'Text:{d}{t}.docx')
                    
                        # print('Nivhe hai upload')
                        c=f'Text:{d}{t}.docx'
                        Output.configure(state='normal')
                        Output.insert(END,'\nWait, Uploading to AWS.....')
                        Output.configure(state='disabled')
                    
                        # print('uploaded')

                    
                
            #========================AWS Link Generate==============
                        
                        s3 = boto3.resource( 
                            "s3",
                            aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                            aws_secret_access_key='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',
                            region_name="ap-south-1",)
                        url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c

                    else:

                        print("Under txt")

                        s3.meta.client.upload_file('random2.txt','anio0007',f'Text:{d}{t}.txt')
                    
                        c=f'Text:{d}{t}.txt'
                        Output.configure(state='normal')
                        Output.insert(END,'\nWait, Uploading to AWS.....')
                        Output.configure(state='disabled')
                        # print('uploaded')
                
            #========================AWS Link Generate==============
                        
                        s3 = boto3.resource( 
                            "s3",
                            aws_access_key_id='AKIAUBLVNIXIBAMOCV4A', 
                            aws_secret_access_key='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',
                            region_name="ap-south-1",)
                        url='https://anio0007.s3.ap-south-1.amazonaws.com/'+c
                    


            
                    
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
        #                 region_name=" ap-south-1",)
        #             url='https://sih-bugaches.s3. ap-south-1.amazonaws.com/'+c
                        
                except:
                    

                    Output.insert(END, 'Unable to upload file')
                    engine.say('Unable to upload file')
                    engine.runAndWait()

               
                # ======================SEND MAIL===========================
                import smtplib
                try:
                    emailpassword = ' Iloveyouadi@143 '
                    emailsend = ' 2002807.it.cec@cgc.edu.in '  # Space should be before and after the ''
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
                                ' 2002807.it.cec@cgc.edu.in ', emailpassword)
                            subject = 'OPTIMAL TECHIES'
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
                                'Mail send successfully!')
                            engine.runAndWait()
                            smtpObj.quit()
                        engine.say(
                                'Now You can choose another file')
                        engine.runAndWait()
                        
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
        # if(pdff == 0):
        #     pass
            # os.remove(duplicatefile)
        # ------------------------------------------------------------------------ekgjaeiorgjaeriojioarjfiod
        clicked.set("CHOOSE FILE FORMAT")
        # label_file_explorer.configure(text="No file Chosen")
        



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
    link = 'https://live-speech2text.netlify.app/'
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
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            Output.configure(state='normal')
            Output.configure(state='disabled')
            print(f"User Said: {query}\n")
            return query

    except Exception as e:
       # print(e)
        pass
    return '0'
def ssstop():
    global sih
    sih=1

def screenshot():
    # global sih
    global query
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


if __name__ == "__main__":

    global query
    global sih
    global pdff
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
    # label_file_explorer = Label(root, text = "No file Chosen", width = 40, height = 1, fg = "blue")
    # label_file_explorer.grid(row=3, column = 0)
    # label_file_explorer.place(x=20,y=705)
    button_explore = Button(root, text = "Browse File", command = browseFiles,width=15, font="Bold",foreground="white",bg="#212529")
    button_explore.grid(row=3, column=0)
    # button_explore.place(x=460,y=700)
    changeOnHover(button_explore, "gray", "#212529")
    button = Button(root, text='Convert and Download', width=20, font="Bold", foreground="white", bg="#212529",command=threading)
    changeOnHover(button, "gray", "#212529")
    button.grid(row=4, column = 0)
    # ***********************Changing into summary******************

    button = Button(root, text='Convert and summarize', width=20, font="Bold", foreground="white", bg="#212529",command=threadingWithSum)
    changeOnHover(button, "gray", "#212529")
    button.grid(row=5, column = 0)


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
    button.grid(row=5, column = 1)
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

    clicked = StringVar()
    clicked.set("CHOOSE FILE FORMAT")
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
    ssstart.grid(row=1, column = 1)
    # downext = Button(root, text='Download extension', width=20, height=1, font="Bold", foreground="white",bg="#212529",command=extensionthread)
    # changeOnHover(downext, "gray", "#212529")
    # downext.grid(row=4, column = 2)
    # sstop = Button(root, text='Stop ScreenShot', width=15, height=1, font="Bold", foreground="white",bg="#212529",command=ssstop)
    # changeOnHover(sstop, "gray", "#212529")
    # sstop.grid(row=4, column = 2)



    # textToSpeech--------------------------------------
    labeltext=Label(root,text='Text To Audio',width=15, font="Bold", foreground="#212529")
    labeltext.grid(row=1,column=2)
    button_explore = Button(root, text = "Choose Text File", command = browseFilesfortext,width=15, font="Bold",foreground="white",bg="#212529")
    button_explore.grid(row=3, column=2)
    # button_explore.place(x=460,y=700)
    changeOnHover(button_explore, "gray", "#212529")
    button = Button(root, text='Convert To Audio', width=20, font="Bold", foreground="white", bg="#212529",command=threadingfortext)
    changeOnHover(button, "gray", "#212529")
    button.grid(row=4, column = 2)
    labeltext=Label(root,text='All right reserved to Optimal Techies \xa9 2022',width=130, font="Bold", foreground="#212529")
    labeltext.place(x=0,y=840)
    # ------------------------------------------------------------
    root.configure(bg='gray19')
    # p1 = PhotoImage(file = 'stotlogo.png')
    # root.iconphoto(False, p1)
    # root.resizable(False, False)
    root.geometry('1414x870')
    # os.chdir('C:/Users/hp/Downloads')
    # print("Current working directory: {0}".format(os.getcwd()))
    mainloop()
