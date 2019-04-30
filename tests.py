import os, sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user.tests import UserTest

if __name__ == '__main__':
    unittest.main()