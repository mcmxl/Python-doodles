#! /usr/bin/env python
# By Micah M. 2018
# House version 1.01.03
# Python 3.6.4


import subprocess
import sys
from time import sleep


def Porch():

    while True:
        choice = input('\nChoose a door. \n1 Front \n2 Exit \n> ')
        if choice == '1':
            livingRoom()
        elif choice == '2':
            raise SystemExit
        else:
            print('Invalid Answer.')


def stairs():

    while True:
        for i in range(1, 7):
            print('%s' % i)
        choice = input('''\nYou\'re in the upstairs hall.
                       \rThere are 6 doors. Choose one. > ''')
        if choice in {'1', '2', '3', '5'}:
#! /usr/bin/env python
# By Micah M. 2018
# House version 1.01.03
# Python 3.6.5

import subprocess
import sys
import time
from time import sleep
import webbrowser


def Porch():

    while True:
        choice = input('\nChoose a door. \n1 Front \n2 Exit \n> ')
        if choice == '1':
            livingRoom()
        elif choice == '2':
            raise SystemExit
        else:
            print('Invalid Answer.')


def stairs():

    while True:
        for i in range(1, 7):
            print('%s' % i)
        choice = input('''\nYou\'re in the upstairs hall.
                       \rThere are 6 doors. Choose one. > ''')
        if choice in {'1', '2', '3', '5'}:
            print('This door is locked.')
        elif choice in {'4', '6'}:
            print('This room is empty.')
        else:
            livingRoom()


def kitchen():

    print('The kitchen is being remodeled. Come back later.\n')
    livingRoom()


def basement():

    while True:
        laundry = input('Do you want to do laundry? \n1 Yes \n2 No \n> ')
        if laundry == '1':
            quarters = int(input('How many quarters do you have? '))
            if quarters < 8:
                print('You need more money.')
            elif quarters >= 8:
                while True:
                    print('Washing')
                    sleep(5)
                    print('Drying')
                    sleep(10)
                    print('Done')
                    livingRoom()
        else:
            livingRoom()


def livingRoom():

    while True:
        roomSelect = ('1 Kitchen', '2 Stairs', '3 Porch', '4 Basement',
                      '5 Browse', '6 Rest')
        for room in roomSelect:
            print('%s' % room)
        room = input('''\nYou\'re in the living room.
                     \rChoose a room or activity. \n> ''')
        if room == '1':
            kitchen()
        elif room == '2':
            stairs()
        elif room == '3':
            Porch()
        elif room == '4':
            basement()
        elif room == '5':
            new = 2
            choice = input('Type site name:\n> ')
            url1 = 'www..com'
            url = 'http://' + url1[:4] + choice + url1[4:]
            webbrowser.open(url, new)
        elif room == '6':
            seconds = int(input('How long? '))
            for i in reversed(range(seconds)):
                time.sleep(1)
                print(i, end='\r\n\n')
        else:
            print('Invalid Answer.')


if __name__ == "__main__":
    Porch()

