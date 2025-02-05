"""
Advanced Computer Language Concepts
Owen K
"""
#imports
import multiprocessing, os, time, random, threading



class my_Modules:

    def __init__(self):

        #get run time
        my_time = time.time()
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
        self.tuple = list(self.tuple)
        self.tuple.append(x)
        self.tuple = tuple(self.tuple)
        self.list.append(x)
        #cant append to a tuple they are not changeable only iterable
    
    def remove_obj(self, x:int):
        #cant remove items from Tuple
        try:
            self.tuple = list(self.tuple)
            self.tuple.pop(x)
            self.tuple = tuple(self.tuple)
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
    

    #week 4 here

    def is_sorted(self, list:list):
            x = 0
            while x < (len(list) - 1):
                if list[x] > list[x+1]:
                    return False
                x +=1 
            
            return True
    


    def fill_list(self, range:int, size:int, type:int):
        list_n = []
        x = 0

        if type == 1:
            while x <= size:
                list_n.append(random.randint(1,range))
                x+=1
        
        elif type == 2:
            while x <= size:
                val = int.from_bytes(os.urandom(1))
                if val >=1 and val <=range:
                    list_n.append(val)
                    x+=1 

        return list_n
    


    #count
    def list_obj(self, list_val:list, list_range: int):
        list_val = sorted(list_val)
        x = 0
        while x <= (list_range - 1):
            x+=1
            print(x," appears >> ",list_val.count(x))
        
        print('\n')
            


    ###End###