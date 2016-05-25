#!/usr/bin/env python

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
def get_command():
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)
	
	# recognize speech using Sphinx
	try:
	    #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
	    return r.recognize_sphinx(audio)
	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print("Sphinx error; {0}".format(e))