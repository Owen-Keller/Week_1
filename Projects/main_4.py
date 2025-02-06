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

    list_3 = mm.fill_list(65535, 100, 1) #create a list with 100 elements from a range 1 65535 using random
    list_4 = mm.fill_list(65535, 100, 2) # create list with 100 elements from a range 1 - 65535 using os.urandom

    list_5 = mm.fill_list(65535, 500, 1)# create a list with 500 elements from a range 1 - 65535 using random
    list_6 = mm.fill_list(65535, 500, 2)# create a list with 500 elements froma range 1 - 65535 using os.urandom





    #print length of the list's and shows the values sorted
    print("List 1 >> ",len(list_1)," :: ",sorted(list_1), "\n")
    print("List 2 >> ",len(list_2), " :: ",sorted(list_2), "\n")

    #using a function in the my_Modules class to print and count items in a list.    
    print("list_1 >>")
    mm.list_obj(list_1, 16)
    print("list_2 >>")
    mm.list_obj(list_2, 16)


    #print lists 3 and 4 like 1 and 2
    

     #print length of the list's and shows the values sorted
    print("List 3 >> ",len(list_3)," :: ",sorted(list_3), "\n")
    print("List 4 >> ",len(list_4), " :: ",sorted(list_4), "\n")

    #using a function in the my_Modules class to print and count items in a list.    
    print("list 3 >>")
    mm.list_obj(list_3, 65535)
    print("list 4 >>")
    mm.list_obj(list_4, 65535)

  
    mm.bogo_sort(list_6)
   

if __name__ == "__main__":
    main()

