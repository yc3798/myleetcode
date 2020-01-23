
# DFS
# 1. build trip hashmap city:dest[....] dest is reversely sorted(aka lexi sorted [C B A ..])
# 2. DFS search using stack
#   pop from top, push trip[curr] to top
class Solution:
    def findItinerary(self, tickets):
        trip = {}
       
        for s,t in tickets:
            if s in trip:
                trip[s].append(t)
            else:
                trip[s] = [t]

        for key in trip:
            trip[key].sort(reverse = True)

        stack = ["JFK"]
        visited = []
        while stack != []:
            # print(stack)
            # print(visited)
            # print(trip)
            curr = stack[-1]
            # has unvisited destination 
            if curr in trip and trip[curr] != []:
                stack.append(trip[curr].pop())

            # does not has next destinations 
            # we want to visit this city last, append to visited
            else:
                visited.append(stack.pop())
        visited.reverse()
        return visited
Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
        
# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.      
                
        