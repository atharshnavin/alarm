import time
import webbrowser
import random
import os
import pyttsx


print "Set alarm"

print "Enter the choice of your alert:"
print "1.Mp3"
print "2.Video"
print "3.Voice"

a=int(raw_input('Enter your choice 1,2 or 3:'))

print "Use the format (Example: 02:40)"
alarm = raw_input("Wake me at >  ") #getting input from user
Time = time.strftime("%H:%M")

if os.path.isfile("youtube.txt") == False: #to check if the text file is in the same location as project.py
	print "Create a text file with links to youtube video and save it in the same location as the program file is saved"

if a==1:
	
	while Time != alarm:
		print "The time is " + Time
		Time = time.strftime("%H:%M")
		time.sleep(1)

	if Time == alarm:
		print "Time to Wake up!"
		os.system("xdg-open /home/atharshnavin/mp3s/brush_your_teeth.mp3")

if a==2:

	with open("youtube.txt") as f: # to open text files with link
		content = f.readlines()

	while Time != alarm:
		print "The time is " + Time
		Time = time.strftime("%H:%M")
		time.sleep(1)

	if Time == alarm:
		print "Time to Wake up!"
		random_video = random.choice(content)
		webbrowser.open(random_video) #the webbrowser library, it opens this youtube video link.
if a==3:
	while Time != alarm:
		print "The time is " + Time
		Time = time.strftime("%H:%M")
		time.sleep(1)

	if Time == alarm:
		print "Time to Wake up!"
		speak_alarm = pyttsx.init()
		command=("time to wake up")
		speak_alarm.say(command)
		speak_alarm.setProperty('rate', 180)
		speak_alarm.runAndWait()




	

