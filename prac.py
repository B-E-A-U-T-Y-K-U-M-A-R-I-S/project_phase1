import speech_recognition as sr
import os


def say(text):
    os.system(f"say {text}")

if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am deskmate A.I")