class Solution:
    def carFleet(self, target, position, speed):

        map1 = {}
        for i in range(len(position)):
            map1[position[i]] = speed[i]
        
        position.sort()
        
        stack =[]
        for j in range(len(position)-1, -1, -1):
            currPos = position[j]
            currSpeed = map1[position[j]]
            reqTime = (target - currPos)/currSpeed

            if not stack or (stack and stack[-1]<reqTime):
                stack.append(reqTime)

        return len(stack)          

    def carFleetPyOpt(self, target, position, speed):          
        cars = sorted(zip(position, speed))
        print(f"Cars={cars}")
        stack = []
        
        # Traverse from the car closest to target
        for pos, spd in reversed(cars):
            time = (target - pos) / spd
            
            # Form a new fleet if it can't catch up
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)       
sol = Solution()
print(sol.carFleet( target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(sol.carFleetPyOpt( target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))