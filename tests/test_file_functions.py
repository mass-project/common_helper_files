'''
Created on Dec 5, 2016

@author: weidenba
'''
import unittest
from common_helper_files.file_functions import human_readable_file_size


class Test_file_functions(unittest.TestCase):

    def test_human_readable_file_size(self):
        self.assertEqual(human_readable_file_size(1024), "1 KB")


if __name__ == "__main__":
    unittest.main()
