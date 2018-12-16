import time
import subprocess

'''
MAIN INFO:
One '-' has the same time length as 3 '.'
In this version they are: 0.3 sec / 0.1 sec
Time between symbols of one letter == time of 1 '.'
Time between symbols of one word == time of 2 '.'
Time between two separate words == time of 6 '.'
'''

DOT_TIME = 0.1 # 0.1 seconds

MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }

def morse_encoder(text):
    text = text.lower()
    text = text.split()
    x = []
    for word in text:
        z = []
        for char in word:
            z.append(MORSE[char])
        x.append(z)
    
    answer = []
    for i in x:
        answer.append(' '.join(i))
    return '   '.join(answer)

def dash_light():
    subprocess.Popen(['termux-torch on'], shell=True)
    time.sleep(DOT_TIME*3)
    subprocess.Popen(['termux-torch off'], shell=True)
    time.sleep(DOT_TIME)

def dot_light():
    subprocess.Popen(['termux-torch on'], shell=True)
    time.sleep(DOT_TIME)
    subprocess.Popen(['termux-torch off'], shell=True)
    time.sleep(DOT_TIME)

def dash_vibrate():
    subprocess.Popen(['termux-vibrate -d ' + str(DOT_TIME*3000)], shell=True)

def dot_vibrate():
    subprocess.Popen(['termux-vibrate -d ' + str(DOT_TIME*1000)], shell=True)

while True:
    method = input('Choose a method: type l to use light, v to use vibrate or e to exit: ')
    if method == 'e':
        exit()
    else:
        your_text = input('Enter your message. Use only A-Z, a-z and 0-9: ')
        encrypted = morse_encoder(your_text)
        if method == 'l':
            for i in encrypted:
                if i == '.':
                    dot_light()
                elif i == '-':
                    dash_light()
                else:
                    time.sleep(DOT_TIME*2)
        else:
            '''
            for i in encrypted:
                if i == '.':
                    dot_vibrate()
                    time.sleep(DOT_TIME)
                elif i == '-':
                    dash_vibrate()
                    time.sleep(DOT_TIME*4)
                else:
                    time.sleep(DOT_TIME*2)
            '''
            print('Sorry, the vibration module is under repair.')