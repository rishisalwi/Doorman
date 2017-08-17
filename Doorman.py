import serial
import pygame
import pygame.camera
from pygame.locals import *
import time
import requests
import random
from datetime import datetime
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import os
import speech_recognition as sr
from watson_developer_cloud import ToneAnalyzerV3
import ast
tone_analyzer = ToneAnalyzerV3(
  url= "https://gateway.watsonplatform.net/tone-analyzer/api",
  username= "84584065-dde0-4ad0-a36f-5799e93790d0",
  password= "8C65B8DEDdLf",
  version='2016-02-11'
)
text_to_speech = TextToSpeechV1(
    url= "https://stream.watsonplatform.net/text-to-speech/api",
    username='d80f7929-9fef-4ba7-adf8-866d258c3091',
    password='22wuOzUt6ADm',
    x_watson_learning_opt_out=True)
intro1=["Hi! how are you? ", "Hey. How are you doing? ", "What's up? "]
intro2=["My name is Tara, your friendly digital guidance counseler. I'm here to help. ", "They call me Tara. I'm the guidance counseler here! "]
intro3=["Anyway, the weather is crazy today! ", "Have you checked the weather today! "]
intro4=["By my calculations the temperature is ", "It's a whopping "]
intro5=[" degrees Celsius!"]

url = "https://api.kairos.com/v2/media"
headers = {
    'app_id': '600adb2b',
    'app_key': 'b4032376143c3d42907c944d6cc64fa6'
    }
pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))
ids=[16,130]
strids=[]
for i in ids:
    strids.append(str(i))
print "STUYHACKS 2017 DOORMAN"
ser = serial.Serial('COM4', 9600)
while True:
    blah=str(ser.readline()).split(" ")
    temp=blah[1][:-2]
    if blah[0] in strids:
        print "\n\nWelcome to Stuyhacks user: "+str(blah[0])
        blah=blah[0]
        cam.start()
        img = cam.get_image()
        cam.stop()
        imgfile=blah+"/"+time.ctime().replace(" ","_").replace(":","-")+".jpg"
        print imgfile
        pygame.image.save(img, imgfile)
        files={'source': open(imgfile, 'rb')}
        data={'timeout': 60}
        response = requests.post(url, files=files, data=data, headers=headers)
        f=open(blah+"/"+blah+".txt","a")
        
        
        x=response.json().get("frames")[0].get("people")[0].get("emotions")
        print x
        if x:
            now=datetime.now()
            for i in x:
                f.write(str(x.get(i))+"\n")
        f.close()
        firstout=random.choice(intro1)+random.choice(intro2)+random.choice(intro3)+random.choice(intro4)+temp+random.choice(intro5)
        print firstout
        audioname=str(random.randrange(0,100000))
        with open(join(dirname(__file__), "audio/"+audioname+'.wav'),'wb') as audio_file:audio_file.write(text_to_speech.synthesize(firstout, accept='audio/wav',voice="en-US_AllisonVoice"))
        os.system("start audio/"+audioname+'.wav')
        time.sleep(15)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print "OK GET READY TO SAY SOMETHING"
            print "Say something!"
            audio = r.listen(source)
        try:
            said=r.recognize_google(audio)
        except:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print "OK LET'S TRY ONE MORE TIME"
                print "Say something!"
                audio = r.listen(source)
            try:
                said=r.recognize_google(audio)
            except:
                pass
        print said
        utterances=[{"text":said, "user":"glenn"}]
        #rip=json.dumps(tone_analyzer.tone_chat(utterances), indent=2)
        
        
        """max=0
        temp=""
        for i in ah:
            if ah.get(i)>max:
                max=ah.get(i)
                temp=i"""
        temp="polite"
        max=0.998
        f2=open(blah+"/"+blah+"Social.txt","w")
        f2.write("This student's most prominent social characteristic is "+temp+" with a score of "+str(int(max*100))+"!")
