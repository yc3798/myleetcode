class Solution:
    # BFS using queue
    # [a,b,c]
    # [b, c, ad, ae, af]
    # [c, ad, ae, af, bd, be, bf] ... 
    # store queue = [string, depth]
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:["a", "b", "c"], 3:["d","e","f"], 4:["g", "h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        if digits == "":
            return []
        
        queue = [(k, 0) for k in d[int(digits[0])]] #(string, depth)
        depth = 0
        
        while True:
            if queue[0][-1] >= len(digits) - 1:
                break
                
            s, depth = queue.pop(0)
            depth += 1
            num = int(digits[depth])       
            for ch in d[num]:
                queue.append((s+ch, depth))
                
        ans = [k[0] for k in queue]
        return ans