class Solution:

    # ========== Final: check for "matches" in reversed string from longest substring ==========
    # i.e, "abcde" -> abcde; abcd, bcde; abc, bcd, cde; ...
    # so we can return if any found, instead of checking all shorter substrings
    # runtime:O(n^2)

    def longestPalindrome3(self, s: str) -> str:
        n = len(s)
        slist = list(s)
        slist.reverse()
        srev = ''.join(str(c) for c in slist)
        l = n
        while l != 0:
            i = 0
            j = i + l
            while not i+l > n:
                # when find the matches, we need to ensure indexes i = n - i
                if srev.find(s[i:j], n - j, n - i) != -1:
                    # print("is palindrome")
                    return s[i:j]
                else:
                    i += 1
                    j += 1
            l -= 1
        return ''

    # ========== improve: check for "matches" in string and its reverse ==========
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        ans = 0
        substring = ''

        slist = list(s)
        slist.reverse()
        srev = ''.join(str(c) for c in slist)
        # when find the matches, we need to ensure indexes i = n - i

        for i in range(n):
            j = i + max(1, ans)
            while j < n + 1:
                # for j in range(i+1, n+1):
                # print(srev, i, j, s[i:j], srev[-j: -i])
                if len(set(s[i:j])) == 1 or srev.find(s[i:j], n - j, n - i) != -1:
                    if j - i > ans:
                        ans = j - i
                        substring = s[i:j]
                j += 1
        return substring

    # ========== brute force ==========
    # checking each substring for palindrome take n, getting all substrings take n^2
    # 0(n^3)
    # space complexity: n^2
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 0
        substring = ''
        i = 0
        j = 1
        while i < n:
            while j < n+1:
                if j - i > ans and self.is_palindrome(s, i, j):
                    ans = j - i
                    substring = s[i:j]
        return substring

    def is_palindrome(self, s: int, i: int, j: int) -> bool:
        target = list(s[i:j])
        target.reverse()
        return list(s[i:j]) == target
