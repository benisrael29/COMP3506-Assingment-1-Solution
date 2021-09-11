from plane_base import PlaneBase


class Plane(PlaneBase):
    """
        Implement all the necessary methods of PlaneBase here
    """
    def getCharacters(self):
         return self.plane_number[0:3]

    def getNumbers(self):
        return self.plane_number[3:7]
