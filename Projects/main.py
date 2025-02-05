"""
Advanced Computer Language Concepts
Owen K
"""
#imports
from my_modules import *
mm = my_Modules()

def main():
   
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

    print("new {}th object added >>\n{}\n{}".format(len(mm.list),mm.list,mm.tuple))

    mm.remove_obj(0) #good news i had dinner!

    print("new list with {} elements >>\n{}\n{}".format(len(mm.list), mm.list,mm.tuple))

        #got bored heres my bogo sort of 50 random objects
    bogo_sort()



def bogo_sort():
    x = 0
    bogo = []
    
    #append 50 random elements to list
    while x <= 50:
        bogo.append(random.randint(0, 50))
        x+=1

    #print value of element in array with "*"

    for _ in range(0, bogo[1]):
        print("*")

        

if __name__ == "__main__":
    main()
