import time
from termcolor import colored


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']

    def running(self):
        while True:
            for el in TrafficLight.__color:
                if el == 'Red':
                    sec = 7
                    while True:
                        print(colored(el, 'red'), colored(sec, 'red'), colored('sec. is left', 'red'))
                        time.sleep(1)
                        sec -= 1
                        if sec < 1:
                            break
                if el == 'Yellow':
                    sec = 2
                    while True:
                        print(colored(el, 'yellow'), colored(sec, 'yellow'), colored('sec. is left', 'yellow'))
                        time.sleep(1)
                        sec -= 1
                        if sec < 1:
                            break
                if el == 'Green':
                    sec = 7
                    while True:
                        print(colored(el, 'green'), colored(sec, 'green'), colored('sec. is left', 'green'))
                        time.sleep(1)
                        sec -= 1
                        if sec < 1:
                            break


switch = TrafficLight()
try:
    while True:
        button = int(input('Press 1 to start, press 0 to exit: '))
        if button == 1:
            switch.running()
        if button == 0:
            break
except ValueError as v:
    print('You have to press "1" or "0" button:', v)
