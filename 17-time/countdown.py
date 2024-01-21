#! python3
# countdown.py - A simple countdown script.

import time, subprocess, sys

if len(sys.argv) < 2:
    print('Usage: countdown.py seconds')
    print('No argument provided. Using default of 60.')
    timeLeft = 60
else:
    timeLeft = int(sys.argv[1])

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file.
if sys.platform.startswith('win32'):
    subprocess.Popen(['start', 'alarm.wav'], shell=True)
elif sys.platform.startswith('linux'):
    subprocess.Popen(['see', 'alarm.wav'])
elif sys.platform.startswith('darwin'):
    subprocess.Popen(['open', 'alarm.wav'])

