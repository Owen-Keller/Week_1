import pyautogui
import numpy as np
import matplotlib.pyplot as plt



def main():
    #pyautogui.moveTo(0,0,duration=0.1)
    x = np.arange(1,11)
    print(x)
    y = x*x
    print(y)

    plt.plot(x, y, color="red")
    plt.show()



if __name__ == "__main__":
    main()