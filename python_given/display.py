from display_base import DisplayRandomBase, DisplayPartiallySortedBase


class DisplayRandom(DisplayRandomBase):
    """
        Implement all the necessary methods here. Need to use self.data which stores the planes to create the sorted list. 
    """
    def getdisplay(self, sortedArry):
        display= ""
        for x in sortedArry:
            display.join(x.plane_number)
            display.join("\n")
        return display

    def quicksort(self,array):
        """Sort the array by using quicksort."""

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x.getTimeAsInt() < pivot.getTimeAsInt():
                    less = less + [x]
                elif x.getTimeAsInt() == pivot.getTimeAsInt():
                    equal = equal + [x]
                elif x.getTimeAsInt() > pivot.getTimeAsInt():
                    greater = greater + [x]
            # Don't forget to return something!
            return self.quicksort(less) + equal + self.quicksort(greater)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array

    def sort(self):
        sortedArray = self.quicksort(self.data)
        print(sortedArray)
        return self.quicksort(self.data)

class DisplayPartiallySorted(DisplayPartiallySortedBase):
    """
        Implement all the necessary methods here
    """

    def getdisplay(self, sortedArry):
        display= ""
        for x in sortedArry:
            display.join(x.plane_number)
            display.join("\n")
        return display

    def sort(self):
        #add two lists to be sorted
        unsortedplanes = self.schedule + self.extra_planes

        #traverse list
        for i in range(1, len(unsortedplanes)):
            key = unsortedplanes[i]
            k = i-1

            while k >= 0 and key.getTimeAsInt() < unsortedplanes[k].getTimeAsInt():
                    unsortedplanes[k + 1] = unsortedplanes[k]
                    k -= 1
            unsortedplanes[k + 1] = key
        print(unsortedplanes)
        return unsortedplanes


def test():
    unsorted = [
        "ABC1234,12:45",
        "QWE4321,13:35",
        "ASD2473,14:32",
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
    print(type(partSort))
    for plane in partSort:
        print(type(plane))

    print("NormSort:")
    print(normSort)
   

if __name__ == "__main__":
    test()
