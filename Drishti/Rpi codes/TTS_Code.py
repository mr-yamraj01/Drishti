import time
import subprocess
from DigitRank import *


def tts(ser0):
    x = ''

    subprocess.Popen(['espeak', '-ven+f3', '-k5', '-s150', 'Welcome to the tutorial for Braille'])

    time.sleep(1)

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alpha:
        x = str(Rank(ch))+'\r'
        ser0.write(x)
        subprocess.Popen(['espeak', '-ven+f3', '-k5', '-s150', 'You pressed the letter' + ch])
        y = ser0.readline().strip()
        while y != 'touchup':
            y = ser0.readline().strip()
        time.sleep(1)
        x = ''

    final_message = 'Congratulations! You have successfully completed the tutorial for learning basic braille script. You are now ready to unlock the full potential of the device!'
    subprocess.Popen(['espeak', '-ven+f3', '-k5', '-s150', final_message])
