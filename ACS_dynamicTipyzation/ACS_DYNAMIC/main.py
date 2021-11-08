# -*- coding: utf-8 -*-
import sys
import string
from extender import *
import time

#from . import extender, container

if __name__ == '__main__':
    start_time = time.time();
    if ((len(sys.argv) != 4)):
        print("Incorrect input! Try following: python main.py -f <inputFileName> <outputFileName>\n"
              "or python main.py -n <sizeOfContainer(1 to 10000)> <outputFileName> if you want to generate all data randomly.")
        exit()
    elif len(sys.argv) == 4 and sys.argv[1] == "-f":
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        inputFile = open(inputFileName)
        data = inputFile.read()
        inputFile.close()
        strArray = data.replace("\n", " ").split(" ")
        print("Processing...\n")
        cont = []
        totalLanguages = container.In(cont, strArray)
    elif len(sys.argv) == 4 and sys.argv[1] == "-n":
        outputFileName = sys.argv[3]
        try:
            size = int(sys.argv[2])
            if (size < 1 or size > 10000):
                print("incorrect numer of figures = "
                      , size, ". Set 0 < number <= 10000\n")
                exit(1)
        except Exception:
            print("Unable to recognize the size of container! Use following format:\n"
                  "python main.py -n <sizeOfContainer(1 to 10000)> <outputFileName>\n")
            exit(1)
        print("Processing...")
        cont = []
        totalLanguages = container.InRnd(cont, size);
    else:
        print("Incorrect input! Try following: python main.py -f <inputFileName> <outputFileName>\n"
              "or python main.py -n <sizeOfContainer (1 to 10000) > <outputFileName> if you want to generate all data randomly.")
        exit()
    ofile = open(outputFileName, 'w')
    container.Write(cont, ofile)
    ofile.write("Sorted container:\n")
    ofile.write("\nCommon function sum: {}\n\n".format(container.CommonC(cont)))
    cont = container.insertion_binary(cont);
    container.Write(cont, ofile);
    ofile.close()
    print("---done in %s seconds ---" % (time.time() - start_time))
    print("Finished!\n")