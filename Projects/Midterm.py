"""
Advanced computer lang
midterm project
Owen A. keller
"""



#imports
from mid_module import *


def main():
    mm = mid_module()
    mm.write_CSV()
    mm.calc_SMA50()
    print(mm.cwd)
    

if __name__ == "__main__":
    main()