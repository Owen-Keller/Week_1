"""
Create A gui with Tkinter
Owen Keller
Advanced Computer logic
"""
#imports
import tkinter as tk

#set global values
import tkinter as tk

#set global values
root = tk.Tk()
message = "="
frame = tk.Frame(root)

Comp_out = tk.Label(frame, text="")
Comp_out.pack(padx=10, pady=10)


def main():
    global frame, root
   
    welcome_message = tk.Label(frame, text="Enter a mathematical statement\n\n Example: 1+2, 1 * 2, 1 / 2, 1 - 2")
    welcome_message.pack(padx=0, pady=30)

    User_input = tk.Entry(frame)
    User_input.pack(padx=20, pady=20)

    def compute():
        mathe = User_input.get()
        numbers, operator = process_input(mathe)
        calc_input(numbers, operator)


    Compute_btn = tk.Button(frame, text="Compute", command=compute)
    Compute_btn.pack(padx=5, pady=5)

    frame.pack(padx=20, pady=20)
    root.mainloop()
    


def process_input(data: str):
   
    char = ""
    char_2 = ""
    numbers = []
    midx = 0
    n = 0
    operator = ''

    data = data.replace(" ","")
    #yes I know slow run time dont mention it its a disgrace
    for _ in data:

        if _.isdigit() is False:
            operator = str(_)
            midx = n
        n+=1
    
    for _ in range(0, midx):
        char+=data[_]
    
    for _ in range(midx+1, len(data)):
        char_2+=data[_]



    numbers.append(char)
    numbers.append(char_2)
    
    return numbers, operator


def test(data:str):

    char = ""
    char_2 = ""
    numbers = []
    midx = 0
    n = 0
    operator = ''

    data = data.replace(" ","")

    for _ in data:

        if _.isdigit() is False:
            operator = str(_)
            midx = n
        n+=1
    
    for _ in range(0, midx):
        char+=data[_]
    
    for _ in range(midx+1, len(data)):
        char_2+=data[_]



    numbers.append(char)
    numbers.append(char_2)
    
    return numbers, operator
# Method to perform calculation with processed input
def calc_input(numbers: list, operator: str):
    global Comp_out
    value = 0
    input_1 = int(numbers[0])
    input_2 = int(numbers[1])

    match operator:
        case "+":
            value = input_1 + input_2
        case "-":
            value = input_1 - input_2
        case "*":
            value = input_1 * input_2
        case "/":
            value = float(input_1) / float(input_2)
            value = round(value, 3)
    
    message = "= " + str(value)
    Comp_out.config(text=message)



if __name__ == "__main__":
    main()