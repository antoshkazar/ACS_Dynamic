import random

#from ACS_DYNAMIC import extender, procedure, OOP, functional


from extender import *


def InRnd(cont, size):
    figNum = 0
    for i in range(size):
        key = random.randint(1, 3)
        if key == 1:
            proc = []
            procedure.InRnd(proc)
            cont.append(proc);
        if key == 2:
            oop = []
            OOP.InRnd(oop)
            cont.append(oop)
        if key == 3:
            func = []
            functional.InRnd(func)
            cont.append(func)
        figNum += 1
    return figNum


def In(cont, strArray):
    arrayLen = int(strArray[0])
    print("array len: ", arrayLen);
    figNum = 0
    i = 1;
    while i < len(strArray):
        currentstr = strArray[i]
        key = int(currentstr)
        if key == 1:
            i += 1
            proc = []
            i = procedure.Read(proc, strArray, i)
            cont.append(proc)
        elif key == 2:
            i += 1
            oop = []
            i = OOP.Read(oop, strArray, i)
            cont.append(oop)
        elif key == 3:
            i += 1
            func = []
            i = functional.Read(func, strArray, i)
            cont.append(func)
        else:
            return figNum
        if i == 0:
            return figNum
        figNum += 1
    return figNum


def Write(cont, ostream):
    ostream.write("Container stores {} shapes:\n\n".format(len(cont)))
    i = 0;
    for shape in cont:
        ostream.write("{}. ".format(i + 1))
        if shape[0] == "procedure":
            procedure.Write(shape, ostream)
        elif shape[0] == "OOP":
            OOP.Write(shape, ostream)
        elif shape[0] == "functional":
            functional.Write(shape, ostream)
        else:
            ostream.Write("Incorrect figure ")
            ostream.Write(shape)
        ostream.write("\n")
        i += 1;
    pass


def CommonC(cont):
    common = 0.0
    for shape in cont:
        if shape[0] == "procedure":
            common += procedure.Common(shape)
        elif shape[0] == "OOP":
            common += OOP.Common(shape)
        elif shape[0] == "functional":
            functional.Common(shape)
        else:
            common += 0.0
    return common


def insertion_binary(cont):
    for i in range(len(cont)):
        language = cont[i]
        lo, hi = 0, i - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if language < cont[mid]:
                hi = mid
            else:
                lo = mid + 1
        for j in range(i, lo + 1, -1):
            cont[j] = cont[j - 1]
        cont[lo] = language
    return cont
