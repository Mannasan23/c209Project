import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path

from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None
song_counter = 0
infoLabel = None

for file in os.listdir('shared_files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " + song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def musicWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectLabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = ("Calibri", 10))
    selectLabel.place(x = 2, y =1)

    listbox = Listbox(window, height = 10, width = 39, activestyle = "dotbox", bg = "LightSkyBlue", borderwidth = 2, font = ("Calibri", 10))
    listbox.place(x = 10, y =18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window, text = "Play", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri", 10), command = play)
    playButton.place(x = 30, y = 200)

    stopButton = Button(window, text = "Stop", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10), command = stop)
    stopButton.place(x = 200, y = 200)

    uploadButton = Button(window, text = "Upload", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10))
    uploadButton.place(x = 30, y = 250)

    downloadButton = Button(window, text = "Download", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10))
    downloadButton.place(x = 200, y = 250)

    infoLabel = Label(window, text = "", fg = "blue", font = ("Calibri", 10))
    infoLabel.place(x = 4, y = 280)


    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()