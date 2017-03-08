# -*- coding: utf-8 -*-

from .context import sample

import unittest


class CoreTestSuite(unittest.TestCase):
    """Test cases for Core"""

    def test_add(self):
        self.assertEqual(sample.add(1,1),2)

    def test_add_not_invalid_result(self):
        self.assertNotEqual(sample.add(1,1),3)

if __name__ == '__main__':
    unittest.main()
