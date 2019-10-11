import collections

def maxLCS(s):
    # Write your code here
    # slice and call helper with all combos
    if len(s) < 2 or collections.Counter(s).most_common(1)[0][1] == 1:
        print("return here")
        return 0 #no possible slice

    i = 1
    j = len(s)
    ans = 0
    while not i == j:
        # print(s[i:j]) # check all combos covered
        ans = max(ans, helper(s[:i],s[i:j]))
        i += 1
    return ans


def helper(s1,s2):
    """
    return cut commonality of s1 and s2
    """
    # start with string of smaller len
    if len(s1) > len(s2): # swap
        temp = s1
        s1 = s2
        s2 = temp

    ans = 0

    # build two counters
    counter1 = collections.Counter(s1)
    counter2 = collections.Counter(s2)
    for item in counter1:
        ans += min(counter1[item],counter2[item])

    return ans


if __name__ == "__main__":
    print(maxLCS("ablkjhc"))