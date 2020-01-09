# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1


# Idea: find the best arrangement
# sort by start time
# if all room occupid, open new room 
# else, assign this meeting to room with earliet end time
# keep track of current meeting end time for each room 

# Naive approach(sorting and hashmap): O(n^2logn)
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if intervals == []:
            return 0
        if len(intervals) == 1:
            return 1

        # sort by start time
        intervals.sort(key = lambda x:x[0])
        # rooms save room : current meeting endtime
        rooms = {1:0} # initially one room
        count = 1
        for m in intervals:
            # available room with earliest finishing time 
            optroom = min(rooms.items(), key = lambda x : x[1]) # O(nlogn)

            # if m starts early than optroom finishing time, allocate new room with m-th meeting
            if optroom[1] > m[0]: 
                count += 1
                rooms[count] = m[1]
            else: # assign this meeting to this room
                rooms[optroom[0]] = m[1]
        # print(count)
        return count

a = [[1,2],[3,4],[5,6]]
Solution().minMeetingRooms(a)
a = [[1,5],[2,3]]
Solution().minMeetingRooms(a)
a = [[2,3],[1,5]]
Solution().minMeetingRooms(a)
a = []
Solution().minMeetingRooms(a)
a = [[1,10],[5,8],[2,3]] 
Solution().minMeetingRooms(a)

Solution()

# improved with Priority Queue(min heap), O(logn) extract, total of O(nlogn)
import heapq
def minMeetingRoomsPQ(intervals):
	intervals.sort(key = lamda x: x[0]) # sort by start time 
	meetingrooms = []
	heapq.heappush(meetingrooms, intervals[0][1]) # key is end time 

	for i in range(1, len(intervals)):
		# check the min item: O(logn)
		if meetingrooms[0] <= intervals[i][0]: # can use this room
			heapq.heappop(meetingrooms)
			heapq.heappush(meetingrooms, intervals[i][1])
		else: # assign new room
			heapq.heappush(meetingrooms, intervals[i][1])
	return len(meetingrooms)
        