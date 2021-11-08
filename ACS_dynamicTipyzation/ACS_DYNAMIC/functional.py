import random


def Read(func, strArray, i):
    if i >= len(strArray) - 3:
        return 0
    func.append("functional")
    func.append(str(strArray[i]))  # typization - static or dynamic
    func.append(bool(strArray[i + 1]))  # LAZYNESS
    func.append(int(strArray[i + 2]))  # TIOBE
    func.append(int(strArray[i + 3]))  # YEAR
    i += 4
    return i


def Write(func, ostream):
    ostream.write(
        "It is a functional Language: typization - {}; Laziness -{}; TIOBE - {}; year - {}".format(func[1], func[2],
                                                                                                     func[3], func[4]))
    pass


def InRnd(func):
    typizRnd = random.choice([True, False])
    func.append("functional")
    if (typizRnd):
        func.append("static")
    else:
        func.append("dynamic")
    func.append(random.choice([True, False]))
    func.append(random.randint(1, 100))
    func.append(random.randint(1960, 2019))
    pass


def Common(func):
    return float(func[4] / 10.0)
    pass
