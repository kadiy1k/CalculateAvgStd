import unittest
import pymysql
from unittest.mock import MagicMock
from unittest.mock import patch


class TestCalculateAvg(unittest.TestCase):
    # MySql database configuration
    def conn(self):
        cursor = pymysql.cursors.DictCursor
        db_config = {'host': 'localhost',
                     'user': 'root',
                     'password': 'Admin123',
                     'db': 'e_store',
                     'charset': 'utf8mb4',
                     'cursorclass': cursor}

        # Mysql database connection
        try:
            connection = pymysql.connect(**db_config)
        except pymysql.Error as conn_error:
            print("MySql database connection unsuccessful")
            exit()


@patch('TestCalculateAvg.pymysql.connect')
def test_mysql_db_connection(self, connect_mock):
    connect_mock.return_value = MagicMock(name='connection_return', return_value="SUCCESS")
    self.assertEqual(1, connect_mock.call_count)


if __name__ == '__main__':
    unittest.main()