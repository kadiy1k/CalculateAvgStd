import unittest
from uberappcode.base_cal_moving import BaseCalculateMoving
from uberappcode.cal_moving_average import CalculateMovingAverage


class TestCalculateMovingA(unittest.TestCase):

    def test_icalculate_moving(self):
        # Validate if the average returned is correct
        BaseCalculateMoving.moving_list = [1, 2, 3, 4]
        calculate_moving_avg = CalculateMovingAverage()
        calculate_moving_avg.icalculate_moving()
        self.assertEqual(2.5, calculate_moving_avg.moving_avg)


class TestCalculateMovingB(unittest.TestCase):

    def test_icalculate_moving(self):
        # Handle None in the list
        BaseCalculateMoving.moving_list = [None]
        calculate_moving_avg = CalculateMovingAverage()
        calculate_moving_avg.icalculate_moving()
        self.assertRaises(TypeError)


class TestCalculateMovingC(unittest.TestCase):

    def test_icalculate_moving(self):
        # Handling empty list as input
        BaseCalculateMoving.moving_list = []
        calculate_moving_avg = CalculateMovingAverage()
        calculate_moving_avg.icalculate_moving()
        self.assertEqual(0, calculate_moving_avg.moving_avg)


class TestCalculateMovingD(unittest.TestCase):

    def test_icalculate_moving(self):
        # Handling if any element in the list has any other data type than int
        BaseCalculateMoving.moving_list = [1, "string_type", None]
        calculate_moving_avg = CalculateMovingAverage()
        calculate_moving_avg.icalculate_moving()
        self.assertRaises(TypeError)


class TestCalculateMovingE(unittest.TestCase):

    def test_calculate_avg_type_error(self):
        # Handle if the argument if not list type
        calculate_moving_avg = CalculateMovingAverage()
        self.assertRaises(TypeError, calculate_moving_avg._calculate_avg, "lll")


class TestCalculateMovingF(unittest.TestCase):

    def test_generate_insert(self):
        # Handling if any element in the list has any other data type than int
        BaseCalculateMoving.moving_list = [1, 2]
        calculate_moving_avg = CalculateMovingAverage()
        test_list = calculate_moving_avg.generate_insert()
        self.assertEqual(3, len(test_list))


if __name__ == '__main__':
    # Specify all the test classes to be run in the array "test_classes_to_run"

    test_classes_to_run = [TestCalculateMovingA, TestCalculateMovingB,
                           TestCalculateMovingC, TestCalculateMovingD,
                           TestCalculateMovingE, TestCalculateMovingF]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
