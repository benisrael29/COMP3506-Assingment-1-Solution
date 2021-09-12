from plane_base import PlaneBase


class Plane(PlaneBase):
    """
        Implement all the necessary methods of PlaneBase here
    """
    def getCharacters(self):
         return self.plane_number[0:3]

    def getNumbers(self):
        return self.plane_number[3:7]

    def getTimeAsInt(self):
        time = self.time[:]
        return int(time.replace(":",""))

    def __lt__(self, other):
        if self.getTimeAsInt()<other.getTimeAsInt():
            return False

        if self.getTimeAsInt == other.getTimeAsInt():
            return True
            
        else:
            return True
