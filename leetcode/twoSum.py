# https://leetcode.com/problems/two-sum

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for x in range(len(nums)):
        for i in range(1, len(nums)):                
            if nums[x] + nums[i] == target:
                print(nums[x], '+', nums[i], '=', nums[x] + nums[i])
                f = nums[x]
                s = nums[i]
                print()
                print('Indeces: [',nums.index(f),']', '[',nums.index(s),']')
                exit()
            else:
                pass
                #print('none')

a = [2, 7, 11, 15]

#twoSum(a, 13)

input(twoSum(List[int], int()))