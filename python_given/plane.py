from plane_base import PlaneBase


class Plane(PlaneBase):
    """
        Implement all the necessary methods of PlaneBase here
    """
    def getCharacters(self):
         return self.plane_number[0:3]

    def getNumbers(self):
        return int(self.plane_number[3:7])

    def getTimeAsInt(self):
        time = self.time[:]
        return int(time.replace(":",""))

    def __lt__(self, other):
        if self.getTimeAsInt() < other.getTimeAsInt():
            return False

        if self.getTimeAsInt == other.getTimeAsInt():

            if self.plane_number[0] == other.plane_number[0]:
                if self.plane_number[1] == other.plane_number[1]:
                    if self.plane_number[2] == other.plane_number[2]:

                        if self.getNumbers == other.getNumbers:
                            return True
                        
                        if self.getNumbers < other.getNumbers:
                            return False

                    if self.plane_number[2] < other.plane_number[2]:
                        return False
                if self.plane_number[1] < other.plane_number[1]:
                    return False
            if self.plane_number[0]< other.plane_number[0]:
                return False

        else:
            return True
