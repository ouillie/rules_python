# The purpose of this test is to exercise the inline 'requirements' attribute
# for the 'pip.parse' module extension. The test logic is not very important.
# What matters is the simple fact that it uses a couple requirements
# that were specified inline in MODULE.bazel.

import unittest

# PyPI packages:
import numpy as np
import requests

class TestStringMethods(unittest.TestCase):

    def test_numpy_imported(self):
        self.assertEqual(np.arange(6).reshape(2, 3)[1][0], 3)
        self.assertEqual(requests.__version__, '2.32.3')

if __name__ == '__main__':
    unittest.main()
