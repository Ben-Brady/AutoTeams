import os
import sys
import threading
import time

from playsound import playsound

import Browser
import Resemble
from ansi import *

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
        else:
            Words[x]=Word + ' '
    return ''.join(Words)

def DetectCaptionsChange():
    global CaptionsChange
    global Captions
    while True:
        with open('captions.txt','r') as x:
            FileContent = x.read()
        if Captions != FileContent:
            Captions = FileContent
            CaptionsChange = True
        time.sleep(0.2)


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

def DemoText():
    x = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Accumsan tortor posuere ac ut consequat semper viverra nam. Purus non enim praesent elementum facilisis leo vel fringilla est. Commodo nulla facilisi nullam vehicula ipsum a arcu. Odio eu feugiat pretium nibh ipsum. Sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu. Facilisis leo vel fringilla est ullamcorper eget. Viverra nibh cras pulvinar mattis nunc sed blandit. Sodales ut eu sem integer vitae justo eget magna. Cras adipiscing enim eu turpis egestas. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi. Venenatis lectus magna fringilla urna porttitor. Dictumst quisque sagittis purus sit amet volutpat. Egestas tellus rutrum tellus pellentesque. Porta non pulvinar neque laoreet suspendisse interdum. Ultricies tristique nulla aliquet enim tortor at auctor. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque. Sapien faucibus et molestie ac. Tincidunt arcu non sodales neque sodales ut etiam sit. Sit amet dictum sit amet justo donec.Duis convallis convallis tellus id interdum velit laoreet id donec. Rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Neque vitae tempus quam pellentesque. Urna duis convallis convallis tellus id interdum. Erat imperdiet sed euismod nisi porta lorem mollis aliquam. Sit amet mauris commodo quis imperdiet massa tincidunt nunc. Duis tristique sollicitudin nibh sit amet commodo nulla. Natoque penatibus et magnis dis. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Ornare arcu odio ut sem nulla pharetra.Risus viverra adipiscing at in tellus integer feugiat scelerisque. Ac placerat vestibulum lectus mauris ultrices eros. Non tellus orci ac auctor. Lacus vel facilisis volutpat est velit. Cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla. Quam id leo in vitae. Tortor at risus viverra adipiscing at in tellus integer. Sed lectus vestibulum mattis ullamcorper. Velit dignissim sodales ut eu sem integer. Pellentesque habitant morbi tristique senectus et netus et.Turpis nunc eget lorem dolor sed viverra. Arcu odio ut sem nulla pharetra. Urna cursus eget nunc scelerisque. Sagittis eu volutpat odio facilisis mauris sit. Dictum fusce ut placerat orci nulla pellentesque dignissim. Dignissim diam quis enim lobortis scelerisque fermentum dui. Ac tortor dignissim convallis aenean et. Nunc id cursus metus aliquam eleifend mi in nulla posuere. Nulla pellentesque dignissim enim sit amet. Posuere urna nec tincidunt praesent semper. Etiam tempor orci eu lobortis elementum nibh. Erat imperdiet sed euismod nisi.Eget nunc lobortis mattis aliquam faucibus purus in massa tempor. In est ante in nibh mauris cursus mattis molestie. Tempor orci eu lobortis elementum nibh. Turpis tincidunt id aliquet risus feugiat in. Laoreet non curabitur gravida arcu ac tortor. Auctor elit sed vulputate mi. Phasellus egestas tellus rutrum tellus. Cras ornare arcu dui vivamus arcu felis bibendum ut tristique. Viverra suspendisse potenti nullam ac tortor vitae. Eu lobortis elementum nibh tellus molestie nunc non blandit massa. Ipsum a arcu cursus vitae congue mauris. Elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus.")
    List = x.split(' ')
    while True:
        with open('captions.txt','w') as x:
            x.write('')
        for x in List:
            time.sleep(0.5)
            with open('captions.txt','a') as File:
                File.write(x+' ')

# threading.Thread(target = DemoText).start()
threading.Thread(target = DetectCaptionsChange).start()
threading.Thread(target = ResembleInput).start()

# Todo: Allow input whilist text generates

print('Input:')
while True:
    CaptionsChange = False
    Output    = FormatPrint(Captions)
    LineCount = Output.count('\n')+1
    print(Output)
    while not(CaptionsChange):
        time.sleep(0.1)