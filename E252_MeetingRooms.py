class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # if si < sj < ei return false
        # sort by key = start time 
        maxendtime = None
        intervals.sort(key = lambda x:x[0])
        for m in intervals:
            if not maxendtime:
                maxendtime = m[1]
            else:
                # if start time < max end time, return false
                # update max end time
                if m[0] < maxendtime:
                    return False
                maxendtime = max(m[1], maxendtime)
        return True