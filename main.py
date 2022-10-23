#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:11:25 2022

@author: leonardoramazzotti
"""

import time
import serial
import subprocess
import json
import os
import keyboard
import platform
from tkinter import *
import webbrowser
import serial.tools.list_ports


def system_rec():
	os = platform.system()

	return os

def keymap_open():

	os_rec= system_rec()

	if os_rec == 'Darwin':

		webbrowser.open('keymapping_files/macos.conf')
			
	elif os_rec == 'Linux':

		webbrowser.open('keymapping_files/linux.conf')

	else:

		webbrowser.open('keymapping_files/win.conf')


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

	root.withdraw()

	os_rec = system_rec()

	if os_rec == 'Darwin':

		with open('keymapping_files/macos.conf') as f:
			map_conf = f.read()

	elif os_rec == 'Linux':

		with open('keymapping_files/linux.conf') as f:
			map_conf = f.read()

	else:

		with open('keymapping_files/win.conf') as f:
			map_conf = f.read()

  
	print("Data type before reconstruction : ", type(map_conf))
	      
	# reconstructing the data as a dictionary
	keymap = json.loads(map_conf)
	  
	print("Data type after reconstruction : ", type(keymap))
	print(keymap)

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



	root.destroy()


	while True:


		det=ser.readline()
		print(type(det))
		print(det)
		data=det.decode()

		data=(int(data))

		print(type(data))
		print(data)

		if '/' in keymap[str(data)]:

			run_software(keymap[str(data)])
		else:
			macro(keymap[str(data)])

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




