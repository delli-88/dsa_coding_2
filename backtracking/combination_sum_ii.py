class Solution:
    def combinationSum2(self, candidates, target):
        
        sol = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], sol)
        return sol

    def backtrack(self, candidates, target, pos, subset, sol):

        if target == 0:
            sol.append(subset[:])
            return

        for i in range(pos, len(candidates)):

            if i > pos and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > target:
                break

            subset.append(candidates[i])

            self.backtrack(candidates, target - candidates[i], i + 1, subset, sol)

            subset.pop()


print(Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5))