class Solution:
    def generateParenthesis(self, n):
        sol = []
        self.helper(n,n,"",sol)
        return sol
    
    def helper(self, open, close, substr, sol):

        if open == 0 and close == 0:
            sol.append(substr)
            return

        if open > 0:
            self.helper(open-1, close, substr+"(", sol)

        if close > open:
            self.helper(open, close-1, substr+")", sol) 
        
        return

print(Solution().generateParenthesis(3))