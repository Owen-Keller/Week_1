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
    list_1 = mm.fill_list(16, 100, 1) # list one is using random
    list_2 = mm.fill_list(16, 100, 2) # list 2 is using os.urandom

    #print length of the list's and shows the values sorted
    print("List 1 >> ",len(list_1)," :: ",sorted(list_1), "\n")
    print("List 2 >> ",len(list_2), " :: ",sorted(list_2), "\n")

    #using a function in the my_Modules class to print and count items in a list.    
    print("list_1 >>")
    mm.list_obj(list_1, 16)
    print("list_2 >>")
    mm.list_obj(list_2, 16)


   

if __name__ == "__main__":
    main()

