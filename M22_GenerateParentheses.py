class Solution:
    # When we are done: left == right == n
    # When we can place ( -> left < n
    # When we can place ) -> right < left
    # define a recursive method to place string

    # time complexity == number of ways to place.
    # Permu(2n, 2)
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def placeParenthesis(s, left, right):
            if left == n and right == n:
                ans.append(s)
                return
            if left < n:
                placeParenthesis(s + '(', left + 1, right)
            if right < left: # unclosed left exists
                placeParenthesis(s + ')', left, right + 1)
        placeParenthesis("", 0, 0)
        return ans