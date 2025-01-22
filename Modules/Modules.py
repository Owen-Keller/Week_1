"""
Advanced Computer Language concepts
Owen Keller
This file is for me to store all the possible functions and classes im working on
"""

#imports
import time, math, os, multiprocessing, threading
class week_1:
    def __init__(self):
        pass

    def hello(self):
        print("Hello world")


    
    def recursion(self, number : int):

        if number == 1:
            print(number)
            return 1
        else:
            print(number)
            return self.recursion(number - 1)


    def Print_square(self, char_1:str, length: int, width: int):

        while length >= 1:
            print(char_1)
            length -= 1
            while width >= length:
                print(char_1)
                width-=1