from display import DisplayPartiallySorted, DisplayRandom


def test():
    unsorted = [
        "ABC1234,12:45",
        "QWE4321,13:35",
        "ASD2473,14:32",
        "ABC1234,12:45",
        "PMG8241,14:55",
        "ANB9206,14:59",
        "MAO3333,15:12",
        "QSA1420,15:15",
        "AXX0023,15:55",
        "QWL0531,23:45"]

    randomList = [
        "ASF6386,23:59",
        "ABC1234,12:45",
        "DWG4314,05:12",
        "QWE4321,13:35",
        "QQQ7299,08:01"
        ]
        
    extra = [
        "ASF6386,23:59",
        "AAA4314,05:12",
        "XXX4321,13:36"
    ]

    partSort = DisplayPartiallySorted (unsorted,extra).sort()
    normSort = DisplayRandom(randomList).sort()

    print("PartSort:")
    print(partSort)


    print("NormSort:")
    print(normSort)


if __name__ == "__main__":
    test()