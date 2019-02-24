#!/usr/bin/env python3
"""By Micah M. 2019
   age100 version 1
   Python 3.7"""



def age100():
    """The year you will be 100"""
    get_name = input('What is your name? ')
    get_age = input('What is your age? ')
    current_year = 2019
    age_100 = (current_year - int(get_age)) + 100
    print(f'{get_name}, you will be 100 years old in {age_100}!')

if __name__ == "__main__":
    age100()
