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


    
    def recursion( self, number : int):

        if self.recursion(number) == 1:
            return 1
        
        else:
            return self.recursion(number - 1)


