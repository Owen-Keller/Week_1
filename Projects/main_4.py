"""
Advanced computer Language
Owen Keller
"""
#imports
from my_modules import *


#init & declare class
mm = my_Modules()


#main function
def main():

    #declare lists
    list_1 = [] # list one is using random
    list_2 = [] # list 2 is using os

    while True:

        list_1.append(random.randint(1,16))

        #using list_1 as break case
        if len(list_1) == 100:
            break

    print(list_1)



   

if __name__ == "__main__":
    main()

