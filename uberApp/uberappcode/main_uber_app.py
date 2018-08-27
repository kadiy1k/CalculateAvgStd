import time
import datetime
import threading
import sys
import pymysql.cursors
from uberappcode.base_cal_moving import BaseCalculateMoving
from uberappcode.cal_moving_average import CalculateMovingAverage
from uberappcode.cal_moving_standard_deviation import CalculateMovingStandardDeviation


def producer_cal_avg():
    """Starts process that continuously inputs random numbers into List"""
    while True:
        movingAvg.generate_insert()
        time.sleep(0.3)


def producer_cal_std():
    """Starts process that continuously inputs random numbers into List"""
    while True:
        movingStd.generate_insert()
        time.sleep(0.4)


def consumer_avg_std():
    """Connects to MySql database and inserts into timestamp, movingavg, movingstd columns"""
    # MySql database configuration
    cursor = pymysql.cursors.DictCursor
    db_config = {'host': 'localhost',
                 'user': 'root',
                 'password': 'Admin123',
                 'db': 'e_store',
                 'charset': 'utf8mb4',
                 'cursorclass': cursor}

    # connecting to Mysql database
    try:
        connection = pymysql.connect(**db_config)
    except pymysql.Error as conn_error:
        print("MySql database connection unsuccessful")
        print(conn_error)
        exit()

    # Inserting records into MySql database
    while True:

        movingAvg.icalculate_moving()
        movingStd.icalculate_moving()

        print("time:", datetime.datetime.now(), " avg:", movingAvg.moving_avg,
              " std:", movingStd.moving_std)

        timestamp = str(datetime.datetime.now())
        movingavg = str(movingAvg.moving_avg)
        movingstd = str(movingStd.moving_std)

        # Inserting timestamp, moving average and moving standard deviation values into database
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `tbl_moving` " \
                      "(`TimeStamp`, `movingavg`, `movingstd`) " \
                      "VALUES (%s, %s, %s)"
                cursor.execute(sql, (timestamp, movingavg, movingstd))
            connection.commit()
        except Exception as e:
            print("Error in MySql database connection: ")
            print(e)
        time.sleep(0.5)
    connection.close()


if __name__ == "__main__":

    # Instantiating the two subclasses
    movingAvg = CalculateMovingAverage()
    movingStd = CalculateMovingStandardDeviation()

    # Spinning up two producer threads and one consumer thread
    consumerThread = threading.Thread(target=consumer_avg_std)
    avgProducerThread = threading.Thread(target=producer_cal_avg)
    stdProducerThread = threading.Thread(target=producer_cal_std)

    # Starting the threads
    try:
        consumerThread.start()
        avgProducerThread.start()
        stdProducerThread.start()
        consumerThread.join()
        avgProducerThread.join()
        stdProducerThread.join()
        print(BaseCalculateMoving.moving_list)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
