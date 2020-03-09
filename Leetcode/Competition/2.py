from typing import List
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # brute force
        # time limitation exceeded
        ans = 0
        length = len(light)
        states = ['0'] * len(light)
        visited = dict()
        for t, i in enumerate(light):
            all_light = True
            key = ''.join(states[:i])
            if key in visited:
                all_light = visited[key]
            else:
                for j in range(i-1):
                    if states[j] == '0':
                        all_light = False
                        break
                visited[''.join(states[:i])] = all_light
            states[i-1] = '2' if all_light else '1'

            j = i
            while j < length and states[j] != '0':
                states[j] = '2' if states[j-1] == '2' else states[j]
                j += 1
            
            all_blue = True
            if states[j-1]=='2':
                while j < length:
                    if states[j] == '1':
                        all_blue = False
                        break
                    j += 1
                ans += 1 if all_blue else 0
        return ans

    def numTimesAllBlue(self, light: List[int]) -> int:
         # time limitation exceeded
        length = len(light)
        states = [0]*length
        light_not_blue = set()
        ans = 0
        for t, i in enumerate(light):
            if i-1>0:
                if states[i-2]==2:
                    states[i-1] = 2
                else:
                    states[i-1] = 1
                    light_not_blue.add(i-1)
            else:
                states[i-1] = 2

            j = i
            while j < length and states[j] > 0:
                if states[j] == 1 and states[j-1]==2:
                    states[j] = 2
                    light_not_blue.remove(j)
                j+=1
            if not light_not_blue:
                ans += 1
        return ans

    def numTimesAllBlue(self, light: List[int]) -> int:
        currMax, ans = 0, 0
        for t, num in enumerate(light):
            currMax = max([currMax, num])
            if currMax == t + 1:
                ans += 1
        return ans

print(Solution().numTimesAllBlue([2,1,3,5,4]))
print(Solution().numTimesAllBlue([3,2,4,1,5]))
print(Solution().numTimesAllBlue([4,1,2,3]))
print(Solution().numTimesAllBlue([2,1,4,3,6,5]))
print(Solution().numTimesAllBlue([1,2,3,4,5,6]))