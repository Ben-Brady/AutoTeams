import requests
import json
import time

from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Load the Pregenerated text
with open('Cache.json') as x:
    Cache = json.load(x)

def UpdateCache():
    with open('Cache.json','w') as x:
        json.dump(Cache,x)

def GenerateClip(Text:str):
    #assert that the text must be a string
    if type(Text) != str:
        raise TypeError
    #Assert the text has a value (No value causes a 404 with resemble)
    if len(Text) == 0:
        raise ValueError
    #Lowercase the text to make it more commom for the cache
    Text=Text.lower()
    #IF text not in the Cache
    if Text not in Cache:
        # ----------- Setup Headers ---------- #
        ProjectID = getenv('RPROID')
        Auth    = {"Authorization"   : "Token token={}".format(getenv("RTOKEN"))}
        Header  = {"Content-Type"    : "applic#ation/json","Authorization"   : "Token token={}".format(getenv("RTOKEN"))}
        Data    = {
            "data": {
                "title" : Text,
                "body"  : Text,
                "voice" : getenv('RVOICE')
                },
            "precision"     : "PCM_16"}
        print(Data)
        URL     = f'https://app.resemble.ai/api/v1/projects/{ProjectID}/clips'

        x = requests.post(URL,headers=Header,json=Data)
        x = json.loads(x.text)

        URL = f"https://app.resemble.ai/api/v1/projects/{ProjectID}/clips/{x['id']}"
        Timeout = 0
        #TODO Improve timeout, currently it's (5+(Word Count * 2))
        Loops   = 5+(len(Text.split(' ')) * 2)
        while Timeout < Loops:
            Timeout+=1
            x = requests.get(URL,headers=Auth)
            x = json.loads(x.text)
            # Check if the clip is finshed being processed
            if x['link'] != None:
                # If so update the cache
                Cache[Text] = x['link']
                break
            time.sleep(1)
    #Write the audio link to a wav file
    with requests.get(Cache[Text]) as x:
        with open('audio.wav','wb') as file:
            file.write(x.content)
    #Update the list of already produced statements
    UpdateCache()

if __name__ == '__main__':
    from playsound import playsound
    GenerateClip(input('Text: '))
    playsound('audio.wav')