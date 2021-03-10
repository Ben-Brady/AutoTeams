import os
import threading
import time

from playsound import playsound

import Browser
import Resemble

Captions = ""
CaptionsChange = False

def FormatPrint(Text:str):
    Width = (os.get_terminal_size()).columns
    Words = Text.split(' ')
    Size = 0
    for x,Word in enumerate(Words):
        Size += len(Word)+1
        if Size > Width:
            Words.insert(x,'\n')
            Size = 0
    return ' '.join(Words)

def DetectCaptionsChange():
    global CaptionsChange
    global Captions
    while True:
        with open('captions.txt','r') as x:
            FileContent = x.read()
        if Captions != FileContent:
            Captions = FileContent
            CaptionsChange = True
        time.sleep(1)


def ResembleInput():
    global Captions
    while True:
        Input = input()
        print('Generating Audio')
        try:
            Resemble.GenerateClip(Input)
        except Exception as e:
            print(e)
        playsound('audio.wav')
        print('Outputting audio')
        Captions = ""

threading.Thread(target = DetectCaptionsChange).start()
threading.Thread(target = ResembleInput).start()

Meeting = True
while True:
    while Meeting:
        CaptionsChange = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print(FormatPrint(Captions),end='\nInput: ')
        while not(CaptionsChange):
            time.sleep(0.5)
