from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([5,4,2,4], 8), 2: ([1,2,3], 6)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        nums, output = self.__testCases[1]
        results = self.__obj.continuousSubarrays(nums = nums)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

    @timeout(0.5)
    def test_case_2(self):
        nums, output = self.__testCases[2]
        results = self.__obj.continuousSubarrays(nums = nums)
        self.assertIsInstance(results, int)
        self.assertEqual(results, output)

if __name__ == '__main__': unittest.main()