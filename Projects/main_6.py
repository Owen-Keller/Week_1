"""
bot poke assignment,

Owen Keller
"""


#imports
import math, csv, random, re

#not sure if using the re library is ok, but ill ask in this class

def main():
    file = open("access.log", "r") # figure relitive path is enough
    
    my_list = []

    #iterate to count lines in original file
    count = 0
    
    #personally I dont like the "for" loops in python they are too ambiguous with how they iterate 
    # I could do this using the "with open" then readlines but you know Im lazy and i typed this on my phone 
    for _ in file:
        count+=1
        if '"BotPoke"' in _:
            continue
        
        my_list.append(_)
    # we dont need the file open anyore since we can work with list content
    file.close()

    print("Lines before remove of 'Botpoke >> '", count)
    print("Lines after remove of 'Botpoke' >> ",len(my_list))

    #Ive had 3 cups coffee and Im a bit chatty in the comments
    

    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') # first regex of string, Ip addresses are kinda annoying but easy google for the pattern

    #I understand most people know the kiss method, but I prefer the lazy meta, Engineers, and especially software engineers should be lazy (Joke) 
    #(Sorry I get very chatty on 3-4 cup of coffee) 
    new_list = []
    for _ in my_list:
        val = pattern.search(_)[0] # sets pattern

        #checks if pattern is not in list, it it isnt in list append the ip
        if val not in new_list:
            new_list.append(val)

    x=1
    for _ in new_list:
        print("count :: {} :: ".format(x),_)
        x+=1

        
        
    

    
    

   
    

        

     
    
        

    



if __name__ == "__main__":
    main()