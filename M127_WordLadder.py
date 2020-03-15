# FIND SHORTEST PATH PROBLEM -> BFS
# return if reach endWord

# Graph: build adjacency list given wordList
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        n = len(wordList[0])
        group = {} # group of words differ at index i
        # group = {(0, 'ot'): ['hot', 'dot', 'lot'], (1, 'ht'): ['hot'], (2, 'ho'): ['hot'], (1, 'dt'): ['dot'], (2, 'do'): ['dot', 'dog'], (0, 'og'): ['dog', 'log', 'cog'], (1, 'dg'): ['dog'], (1, 'lt'): ['lot'], (2, 'lo'): ['lot', 'log'], (1, 'lg'): ['log'], (1, 'cg'): ['cog'], (2, 'co'): ['cog']}
        
        for w in wordList:
            for i in range(n):
                key, part = i, w[:i] + w[i+1:]
                if (key, part) in group:
                    group[(key, part)].append(w)
                else:
                    group[(key, part)] = [w]
        # (word, last-modified index, path)
        queue = [(beginWord, None, [])]
        
        while queue != []:
            curr, prevpos, path = queue.pop(0)
            # we reach the target word in BFS search, return 
            if curr == endWord:
                return len(path) + 1 
            for i in range(n):
                # avoid chaging previously changed index at prevpos
                if i != prevpos:
                    temp = curr[:i] + curr[i+1:]
                    # append all possible next words to queue(except for current word)
                    # delete entry from group since in BFS we do not want to 
                    # re-visit a visited word

                    # previously visit gurantees shortest path 
                    if (i, temp) in group:
                        queue.extend([(ch,i,path + [ch]) for ch in group[(i, temp)] if i != ch])
                        del group[(i, temp)]

        return 0
                            
                
            
        