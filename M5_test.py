import unittest
from M5_PalindromicSubstr import Solution

class TestM5(unittest.TestCase):

    def test_nonpalin(self):
        s = 'abc'
        result = Solution().longestPalindrome3(s)
        self.assertEqual(result, 'a')

    def test_empty(self):
        s = ''
        result = Solution().longestPalindrome3(s)
        self.assertEqual(result, '')

    def test_repeat(self):
        s = 'bbaaaaaaaaaaaaaaa'
        result = Solution().longestPalindrome3(s)
        self.assertEqual(result, 'aaaaaaaaaaaaaaa')

    def test_spec(self):
        s = 'abcklcba'
        result = Solution().longestPalindrome3(s)
        self.assertEqual(result, 'a')

    def test_palin(self):
        s = 'afsdfsdhjkabcdeedcbaadfsd'
        result = Solution().longestPalindrome3(s)
        self.assertEqual(result, 'abcdeedcba')


if __name__ == '__main__':
    unittest.main()

