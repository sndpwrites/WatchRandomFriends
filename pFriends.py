import os
import random

season = [f for f in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), f))]
os.chdir(random.choice(season))
episode = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
Fepisode = random.choice(episode)
print Fepisode[-3:]
if Fepisode[-3:] == "mkv":
    os.system("vlc " + Fepisode)
