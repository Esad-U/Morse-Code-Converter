from Morse import *
import RPi.GPIO as GPIO
from time import sleep

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    pin = 3
    GPIO.setup(pin, GPIO.OUT)
    DOT = 0.075  # Constant for duration of one dot in Morse Code
    cvt = Morse(pin, DOT)

    sentence = input("Enter the sentence to be converted (all lower case, use only '.' as punctuation): ")
    cvt.convert_and_play(sentence)
