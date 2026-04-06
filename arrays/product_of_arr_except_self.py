class Solution:
    def productExceptSelf(self, nums):

        left_prefix = [0]*len(nums)
        right_prefix = [0]*len(nums)
        prefix_sum = 1
        for i in range(len(nums)):
            prefix_sum*= nums[i]
            left_prefix[i] = prefix_sum

        prefix_sum = 1
        for j in range(len(nums)-1, -1, -1):
            prefix_sum*= nums[j]
            right_prefix[j] = prefix_sum
        
        sol = []
        for k in range(len(nums)):
            left = 1
            if k>0:
                left = left_prefix[k-1]
            
            right = 1
            if k<len(nums)-1:
                right = right_prefix[k+1]

            sol.append(left * right)
        return sol


    def productExceptSelfOpti(self, nums):

        right_prefix_arr = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right_prefix_arr[i] = right_prefix_arr[i+1] * nums[i+1]
        
        left_prefix = 1
        sol = []
        for j in range(len(nums)):
            sol.append(left_prefix * right_prefix_arr[j])
            left_prefix = left_prefix * nums[j]
        
        return sol
    
    def productExceptSelfOpti2(self, nums):

        sol  = [1] * len(nums)
        left_prefix = 1
        for i in range(len(nums)):
            sol[i] = left_prefix
            left_prefix *= nums[i]
        
        right_prefix = 1
        for j in range(len(nums)-1, -1, -1):
            sol[j] = sol[j] * right_prefix
            right_prefix*=nums[j]
        
        return sol

sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))
print(sol.productExceptSelfOpti(nums = [1,2,3,4]))
print(sol.productExceptSelfOpti2(nums = [1,2,3,4]))