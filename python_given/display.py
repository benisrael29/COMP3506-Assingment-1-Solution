from display_base import DisplayRandomBase, DisplayPartiallySortedBase


class DisplayRandom(DisplayRandomBase):
    """
        Implement all the necessary methods here. Need to use self.data which stores the planes to create the sorted list. 
    """

    def sort1(self):

        #traverse list
        for i in range(1, len(self.data)):
            key = self.data[i]
            k = i-1

            while k >= 0 and key > self.data[k]:
                    self.data[k + 1] = self.data[k]
                    k -= 1
            self.data[k + 1] = key
        return self.data


    def quick(self,array):
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
            return self.quick(less) + equal + self.quick(greater)  
        else: 
            return array

    def sort(self):
        queue = self.quick(self.data)
        return queue

class DisplayPartiallySorted(DisplayPartiallySortedBase):
    """
        Partial sort method, combines seld.schedule and self.extra_planes 
        and sorts the resulting list.

        return: sorted arrray of planes
    """
    def sort(self):

        unsortedplanes = self.schedule + self.extra_planes
        
        for i in range(1, len(unsortedplanes)):
            key = unsortedplanes[i]
            k = i-1

            while k >= 0 and key > unsortedplanes[k]:
                    unsortedplanes[k + 1] = unsortedplanes[k]
                    k -= 1
            unsortedplanes[k + 1] = key
        return unsortedplanes
