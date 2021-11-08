import random


def Read(proc, strArray, i):
    if i >= len(strArray) - 2:
        return 0
    proc.append("procedure")
    proc.append(bool(strArray[i]))  # abcstract or not
    proc.append(int(strArray[i + 1]))  # TIOBE
    proc.append(int(strArray[i + 2]))  # YEAR
    i += 3
    return i


def Write(proc, ostream):
    ostream.write("It is a procedure Language: abstract - {}; TIOBE - {}; year - {}".format(proc[1],
                                                                                              proc[2], proc[3]))
    pass


def InRnd(proc):
    proc.append("procedure")
    proc.append(random.choice([True, False]))
    proc.append(random.randint(1, 100))
    proc.append(random.randint(1960, 2019))
    pass


def Common(proc):
    return float(proc[3] / 8.0)
    pass
