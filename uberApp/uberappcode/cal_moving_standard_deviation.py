from uberappcode.base_cal_moving import BaseCalculateMoving
import random
import statistics


class CalculateMovingStandardDeviation(BaseCalculateMoving):

    def __init__(self):
        # self.moving_list = []
        self.moving_std = 0

    def generate_insert(self):
        # Function to generate a random number and insert into list
        random_number = random.randint(1, 1000)
        BaseCalculateMoving.moving_list.append(random_number)
        return BaseCalculateMoving.moving_list

    def _calculate_std(self, new_list):

        try:
            if type(new_list) is not list or new_list is None:
                raise TypeError
        except TypeError as e:
            print(e)

        list_length = len(new_list)
        if list_length < 2 or None in new_list:
            return 0
        std_dev = statistics.stdev(new_list)
        return std_dev

    def icalculate_moving(self):
        self.moving_std = self._calculate_std(BaseCalculateMoving.moving_list)
