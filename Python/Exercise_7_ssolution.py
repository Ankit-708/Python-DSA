# Healthy programmer

# water - water.mp3 (3.5 litres) - drank - log-every 40 min
# eyes - eyes.mp3 - every 30 min - eyedone - log - every 30 min
# physical activity - physical.mp3 every -45 min -exdone -log

# rules
# pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_time(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n") # it will print message

if __name__=='__main__':
    # musiconloop("water.mp3", "stop")  #that mp3 file should present in the file

    init_water = time()
    init_eye = time()
    init_exercise = time()
    watersecs= 5
    exercisesecs = 10
    eyesecs = 20

    while True:
        if time() - init_water > watersecs:
            print("water dranking time. Enter 'drank' to stop this alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_time("drank water at")

        if time() - init_eye > eyesecs:
            print("eye exercise time. Enter 'doneeye' to stop this alarm.")
            musiconloop('eye.mp3', 'doneeyes')
            init_eye = time()
            log_time("eye relaxed at")

        if time() - init_exercise > exercisesecs:
            print("physical activity time. Enter 'donephy' to stop this alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_time("physical activity done at")