"""
Advanced Computer Language Concepts
Owen K
"""
#imports
import my_modules

def main():
    mm = my_modules.my_Modules()
    mm.recursive_Math(990)
    
    #week 3 content
    print("\n\n\nWeek 3")
    ### print list and tuple
    print(mm.list,"\n",mm.tuple)
    #retrieve the 3rd object in the tuple and list using the index value
    print("Index of 2.\n3rd Object in the Tuple and List >> ",mm.Return_index(2))

    #technically not sorting the list but It is a cool concept pushing the theory of multiple dimensions and infinite worlds.  
    print("Random >> ",mm.bogo_sort())

    ###TUPLES CAN NOT HAVE ELEMENTS REMOVED!?! ### CLEARLY I know lol ;) ;) ####
    mm.add_obj("cheese burger") # I got a bit hungry

    print("new {}th object added >> {}".format(len(mm.list),mm.list))

    mm.remove_obj(0) #good news i had dinner!

    print("new list with {} elements >> {}".format(len(mm.list), mm.list))





if __name__ == "__main__":
    main()
