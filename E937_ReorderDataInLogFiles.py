# 937. Reorder Data in Log Files

# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  
# It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
# The digit-logs should be put in their original order.
# Return the final order of the logs.


# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

class Solution:
    
    # for each log in logs, if letterlog, insert in previous letterlog
    # use pos to track position of last letterlog
    def reorderLogFiles(self, logs):
        pos = -1 # pos of last letterlog
        ans = []
        for log in logs:
            if log[log.index(" ") + 1].isalpha():       
                if pos == -1: # insert at front
                    ans.insert(0, log)
                else:
                    k = pos
                    while k >= 0 and (ans[k][ans[k].index(" ") + 1:] > log[log.index(" ") + 1:] or (ans[k][ans[k].index(" ") + 1:] == log[log.index(" ") + 1:] and ans[k][:ans[k].index(" ")] > log[:log.index(" ")])):
                        k -= 1
                    ans.insert(k + 1, log)
                pos += 1
            else:
                ans.append(log)
        return ans
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Solution().reorderLogFiles(logs)