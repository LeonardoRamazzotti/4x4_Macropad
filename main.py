#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:11:25 2022

@author: leonardoramazzotti
"""

import time
import serial
import subprocess
import os
import keyboard
from tkinter import *
import serial.tools.list_ports

def port_define(str_port):

	for element in str_port :

		if element == ' ':
			port_splitted=str_port.split(' ')

			print(type(port_splitted))
			print(port_splitted)

			return port_splitted[0]

def show():
    label.config( text = clicked.get() )

def port_list():
	ports=serial.tools.list_ports.comports(include_links=False)

	print(type(ports))
	return ports

def macro(input):

	keyboard.press_and_release(input)
	

def run_software(path):
		try:
			
			print("Opening...")
			os.system("open "+path)
			
		except:
			print("Program not Open")


def run():

	keymap={
		0:'/Applications/"Google Chrome.app"',
		1:'/Applications/"Sublime Text.app"',
		2:'/Applications/"Spotify.app"',
		3:'/System/Applications/Utilities/Terminal.app',
		4:'/Applications/"Microsoft Word.app"',
		5:'/Applications/"Microsoft Excel.app"',
		6:'windows+space',
		7:'fsdfsdf',
		8:'fsdfsdf',
		9:'fsdfsdf',
		10:'fsdfsdf',
		11:'/Applications/"Sublime Text.app"',
		12:'/Applications/"Spotify.app"',
		13:'/System/Applications/Utilities/Terminal.app',
		14:'/Applications/"Microsoft Word.app"',
		15:'/Applications/"Microsoft Excel.app"',
		}

	selected= str(clicked.get())

	port= port_define(selected)


	print(port)
	try:
		ser = serial.Serial(port, 9600) # open serial port
		print(ser.name)       # check which port was really used
		
		if 'n/a' in port:
			label_error=Label(root,text='Comuniocation Error: Wrong Port')
			label_error.pack()

	except:
		label_error=Label(root,text='Comunication Error: No Port Selected')
		label_error.pack()






	while True:


		det=ser.readline()
		print(type(det))
		print(det)
		data=det.decode()

		data=(int(data))

		print(type(data))
		print(data)

		if '/' in keymap[data]:

			run_software(keymap[data])
		else:
			macro(keymap[data])

	ser.close()



root=Tk()
root.title('Matrix Solver')
root.geometry('400x550')
root.resizable(False,False)

label_port= Label(root,text='Select Port')
label_port.pack()


  
# Dropdown menu options
options = port_list()
 
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( '-' )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

start=Button(root,text="Run", command= run)
start.pack()

	

	
root.mainloop()




