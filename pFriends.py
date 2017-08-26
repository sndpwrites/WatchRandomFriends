import os
import random

season = [f for f in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), f))]
os.chdir(random.choice(season))
episode = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
Fepisode = random.choice(episode)
Fvideoformat = ["mkv", "mp4"]
if Fepisode[-3:] in Fvideoformat:
    os.system("vlc " + Fepisode)
