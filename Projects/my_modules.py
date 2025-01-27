"""
Advanced Computer Language Concepts
Owen K
"""
#imports
import multiprocessing, os, time, random, threading



class my_Modules:

    def __init__(self):
        self.mp = multiprocessing


    
    def Count(self, number:int):

        while number != 0:
            print(number)
            number-=1

    
    def make_Job(self, number:int):
        my_job = self.mp.Process(target=self.Count, args=(number,))

        my_job.start()

        my_job.join()


    def recursive_Math(self, number:int):
        if number ==1:
            print("{} ::{}".format(number, number))
            return 1
        
        print("{} :: {}".format(number,(number -1)/number))
        return self.recursive_Math(number-1)

    ###End###