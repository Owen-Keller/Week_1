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
        value = int.from_bytes(os.urandom(1), byteorder='big')

        if value >= 1 and value <=16:
            list_1.append(random.randint(1,16))
            list_2.append(value)

        #using list_1 as break case
        if len(list_1) == 100:
            break
    

    #print length of the list's and shows the values sorted
    print(len(list_2)," :: ",sorted(list_2), "\n")
    print(len(list_1), " :: ",sorted(list_1), "\n")



   

if __name__ == "__main__":
    main()

