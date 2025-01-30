"""
Advanced Computer Language Concepts
Owen K
"""
#imports
import multiprocessing, os, time, random, threading



class my_Modules:

    def __init__(self):
        self.mp = multiprocessing
        self.list = ["A","B","C","D","E","F","G","H","I","J"]
        self.tuple = ("J","I","H","G","F","E","D","C","B","A")

    
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
    

    def sort_List(self):

        return sorted(self.tuple)
    
    def Return_index(self, x:int):
        return self.tuple[x], self.list[x]
    
    def add_obj(self, x:object):
        self.list.append(x)
        #cant append tyo a tuple they are not changeable only iterable
    
    def remove_obj(self, x:int):
        #cant remove items from Tuple
        try:
            self.list.pop(x)
        except:
            print("Index out of range")

    def bogo_sort(self):
        lst = []
        x = len(self.list) -1
        
        while True:
            Object = self.list[random.randint(0, x)]

            if Object in lst:
                continue

            lst.append(Object)

            if len(lst) == 10:
                break


        return lst


    ###End###