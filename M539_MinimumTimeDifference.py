class Solution:
    # Sort
    # then calculate pairwise different
    # O(nlogn)
    # 注意处理时间差 eg, 23:59 -> 00:00 = 1 min 
    # 如何处理 diff = min(diff, 24 * 60 - diff)
    def findMinDifference(self, timePoints: List[str]) -> int:

        def calculateMin(a): # return minute 
            ahour, amin = a.split(":")
            res = int(ahour) * 60 + int(amin) 
            return int(ahour) * 60 + int(amin) 
        
        minutes = [calculateMin(k) for k in timePoints]
        minutes.sort()
        
        diff = [abs(minutes[k+1] - minutes[k]) for k in range(len(minutes) - 1)]
        diff.append(abs(minutes[0] - minutes[-1]))
        mindiff = min(diff, key = lambda k: min(k, 24 * 60 - k))
        

        return min(24 * 60 - mindiff, mindiff)