import random
import sys
from uberappcode.base_cal_moving import BaseCalculateMoving


class CalculateMovingAverage(BaseCalculateMoving):
    # Inserts random number to a list and calculates average for all elements in list
    def __init__(self):
        # self.moving_list = []
        self.moving_avg = 0

    def generate_insert(self):
        """Append random number into moving list and returns new list"""
        random_number = random.randint(0, 1000)
        try:
            BaseCalculateMoving.moving_list.append(random_number)
        except MemoryError as error:
            print("Moving List has reached max memory ERROR: " + error)
        return BaseCalculateMoving.moving_list

    def _calculate_avg(self, new_list):
        """Takes list as input and returns average for all elements in the list"""
        try:
            if type(new_list) is not list or new_list is None:
                print("TypeError: Input parameter should be list...")
                sys.exit()
        except TypeError as e:
            print(e)
        list_length = len(new_list)

        if list_length == 0 or None in new_list:
            return 0
        elif all(isinstance(element, int) for element in new_list):
            list_sum = sum(new_list)
            avg = (list_sum / list_length)
            return avg
        return 0

    def icalculate_moving(self):
        """Overrides the method from base class to calculate average"""
        self.moving_avg = self._calculate_avg(BaseCalculateMoving.moving_list)
