import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox

import speech_recognition as sr
import time

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("speak anything.....")
		audio = r.listen(source)
		try:
			print("Regognizing....")
			text = r.recognize_google(audio)
			print('You said: ' + text)
			if text == "stop":
				print("Program will exit.")
				break
			else:
				window = Tk()
				window.geometry("700x600")
				try:
					app_id = " R25A4E-A53TPH4LLL"
					client = wolframalpha.Client(app_id)
					res = client.query(text)
					answer = next(res.results).text
					print("Answer from Wolfram|Alpha:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					window.after(5000, lambda: window.destroy())
					mainloop()
				except Exception as e:
					print("No results from Wolfram|Alpha. Trying wikipedia...")
					answer = wikipedia.summary(text)
					print("Answer from Wikipedia:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					window.after(500000, lambda: window.destroy())
					mainloop()
		except Exception as e:
			print(e)
			answer = "Sorry, you were not audible "
			print(answer)
