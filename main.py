import sys,pygame
from window import *
from physics import *

def main(argv):
    print(argv)
    data,size = our_function()
    print(size)
    run_window("McGill Physics Hackaton 2020",data,size)

if __name__ == "__main__":
    main(sys.argv)
