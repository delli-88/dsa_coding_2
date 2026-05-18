class Solution:
    def combinationSum(self, candidates, target):
        sol = []

        def backtrack(idx, subset, total):
            if total == target:
                sol.append(subset[:])
                return

            if idx == len(candidates) or total > target:
                return

            # take current candidate
            subset.append(candidates[idx])
            backtrack(idx, subset, total + candidates[idx])

            # backtrack (undo choice)
            subset.pop()

            # skip current candidate
            backtrack(idx + 1, subset, total)

        backtrack(0, [], 0)
        return sol


print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))