import time

from playsound import playsound

CLEAR= "\033[2J"
CLEAR_AND_RETURN="\033[H"

def alarm(seconds):
    time_elapsed=0

    print(CLEAR)
    while time_elapsed< seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left = seconds - time_elapsed
        hours_left=time_left//3600
        minute_left= time_left//60
        seconds_left=time_left%60



        print(f"{CLEAR_AND_RETURN}Alarm will sonund in {hours_left:02d}:{minute_left:02d}:{seconds_left:02d}")
        
    playsound("sound.mp3")

hours=int(input("How mony hours: "))
minutes=int(input("How many minutes: "))
seconds=int(input("How many seconds: "))
total_seconds=hours*3600 + minutes*60+ seconds
alarm(total_seconds)
