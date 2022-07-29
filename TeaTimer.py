### Tea Timer
### By: VikingIwan

## Imports
import time as time
from playsound import playsound

## Variables
timer = 0.5 # Time in Minutes

## Functions
def runTimer(timer):
	time.sleep((timer * 60))
	playsound('res/ping.mp3')
	playsound('res/ping.mp3')
	playsound('res/ping.mp3')

def main():
	print("Timer has been started for " + str(timer) + " minutes")
	runTimer(timer)
	print("It's tea time!")


## Runtime Baby ##
main()