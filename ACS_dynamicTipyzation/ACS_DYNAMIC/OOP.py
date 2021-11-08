import random


def Read(oop, strArray, i):
    if i >= len(strArray) - 2:
        print("wrong len")
        return 0
    oop.append("OOP")
    oop.append(str(strArray[i]))  # inheritance - one, plural or interface
    oop.append(int(strArray[i + 1]))  # TIOBE
    oop.append(int(strArray[i + 2]))  # YEAR
    i += 3
    return i


def Write(oop, ostream):
    ostream.write(
        "It is a OOP Language: inheritance - {}; TIOBE - {}; year - {}".format(oop[1], oop[2], oop[3]))
    pass


def InRnd(oop):
    oop.append("OOP")
    inheritancernd = random.randint(1, 3)
    if (inheritancernd == 1):
        oop.append("one")
    elif (inheritancernd == 2):
        oop.append("plural")
    elif (inheritancernd == 3):
        oop.append("interface")
    oop.append(random.randint(1, 100))
    oop.append(random.randint(1960, 2019))
    pass


def Common(oop):
    return float(oop[3] / 3.0)
    pass
