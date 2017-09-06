import os
import random
from Tkinter import *
import tkFileDialog
window = Tk()

def getLocation():
    f = open('location.txt','r')
    content = f.read()
    print content
    f.close()
    return content
    
def saveLocation(pPath):
    with open('location.txt','r+') as f:
        content = f.read()
        f.seek(0)
        f.write(pPath)
        f.truncate()

def getPath():
    folderpath=tkFileDialog.askdirectory(parent=window, title='Choose location to desired folder')
    abs_path=os.path.abspath(folderpath)
    return abs_path

def btnGo():
    os.chdir(getLocation())
    season = [f for f in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), f))]
    os.chdir(random.choice(season))
    episode = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    Fepisode = random.choice(episode)
    Fvideoformat = ["mkv", "mp4"]
    if Fepisode[-3:] in Fvideoformat:
        os.system("vlc " + Fepisode)
        print("vlc " + Fepisode)

def btnChange():
    saveLocation(getPath())
    window.update()

def pGUI(content):
    window.title("pFriends")
    l1=Label(window, text="Enter series folder location")
    l1.pack(side=TOP)
    e1=Entry(window)
    e1.insert(END, content)
    e1.pack(side=TOP)
    b1=Button(window, command=btnGo, text="Go!")
    b1.pack(side=BOTTOM)
    b2=Button(window, command=btnChange, text="Change Location")
    b2.pack(side=BOTTOM)


content=getLocation()
if (content==''):
    getPathHere=getPath()
    saveLocation(getPathHere)
else:
    pGUI(content)
    

window.mainloop()
