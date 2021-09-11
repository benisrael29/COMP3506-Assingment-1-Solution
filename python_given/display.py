from display_base import DisplayRandomBase, DisplayPartiallySortedBase


class DisplayRandom(DisplayRandomBase):
    """
        Implement all the necessary methods here. Need to use self.data which stores the planes to create the sorted list. 
    """

    def merge(self, left, right):
        result = [] 
        x, y = 0, 0
        for k in range(0, len(left) + len(right)):
            if x == len(left): # if at the end of 1st half,
                result = result + right[y] # add all values of 2nd half
                y += 1
            elif y == len(right): # if at the end of 2nd half,
                result = result + left[x] # add all values of 1st half
                x += 1
            elif right[y].time < left[x].time:
                result= result + right[y] 
                y += 1
            else:
                result = result + left[x]
                x += 1
            return result

    def sort(self):
        length = len(self.data)
        size = 1
        while size < length:
            size+=size # initializes at 2 as described
            for pos in range(0, length, size):
                start = pos
                mid  = pos + int(size / 2)
                end = pos + size
                left = self.data[ start : mid ] 
                right = self.data[ mid : end ] 
                self.data[start:end] = self.merge(left, right)
                return self.data


class DisplayPartiallySorted(DisplayPartiallySortedBase):
    """
        Implement all the necessary methods here
    """
    def sort(self):
        return 0