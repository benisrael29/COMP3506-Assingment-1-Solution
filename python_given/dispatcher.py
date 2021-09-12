
from dispatcher_base import DispatcherBase


class Dispatcher(DispatcherBase):
    """
        Implement all the necessary methods here
    """
    def __init__(self):
        """
        Initialize the data structure to store planes
        """
        # raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """
        Compute the number of the planes in the system

        :return: the number of the planes in the system
        """
        return 0

    def is_empty(self):
        """
        Return True if there are no planes in the system
        """
        return len(self) == 0

    def add_plane(self, plane_number: str, time: str):
        """
        Add a plane to the system.
        The complexity must be O(n)

        :param plane_number: string with 3 letters, followed by 4 numbers.
                             Example: "ABC1243", "ENC3455"
        :param time: string, represents time in 24h format.
                     Example: "9:24", "15:32"
        :return:
        """
        return 

    def allocate_landing_slot(self, current_time: str):
        """
        Allocate the landing slot to the next plane in line if it is already waiting
        or if it arrives no later than 5 minutes from the current time.
        Remove the plane that has been granted a landing slot and return its number
        Otherwise return None

        The complexity must be O(1)

        :param current_time:string, represents the current time in 24h format.
                            Example: "9:24", "15:32"
        :return: Plane number or None
        """
        return None

    def emergency_landing(self, plane_number: str):
        """
        Find and remove a plane by its number.
        The complexity must be O(n)

        :param plane_number: string with 3 letters, followed by 4 numbers.
                             Example: "ABC1236", "ENC3455"
        :return: Plane number or None
        """
        return None

    def is_present(self, plane_number: str):
        """
        Returns True if the plane is in the system, otherwise return False

        :param plane_number: string with 3 letters, followed by 4 numbers.
                             Example: "ABC1235", "ENC3454"
        :return: True/False
        """
        return True

