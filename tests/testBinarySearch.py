import unittest
from binarySearch import bsearch

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.l = [2, 3, 7, 8, 9, 12, 17]
        self.start = 0
        self.end = len(self.l) - 1

    def testFind2(self):
        assert bsearch(self.l, 2, self.start, self.end) == 0

    def testFind17(self):
        assert bsearch(self.l, 17, self.start, self.end) == self.end

    def testFind8(self):
        assert bsearch(self.l, 8, self.start, self.end) == 3

    def testFindNonExistentElement(self):
        assert bsearch(self.l, 99, self.start, self.end) == -1