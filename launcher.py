import os, sys, json
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

titletext = canvas.create_text(200, 10, text="ProjectLoader v1.0.0", anchor=N, font=("", 25))
subtitle = canvas.create_text(200, 50, text="By Johnny", anchor=N, font=("times", 20))
bodytext = canvas.create_text(200, 150, text="Couldn't load projectinfo.json")

#try:
if(True):
	project =  open("projectinfo.json").read()
	projectinfo = json.loads(project)

	canvas.itemconfigure(bodytext, text=projectinfo["bodytext"])
	canvas.itemconfigure(titletext, text=projectinfo["name"])
#except:
#	print("Error")

startbutton = canvas.create_rectangle(10, 200, 390, 290, outline="#4286f4", fill="#4286f4")
root.mainloop()
