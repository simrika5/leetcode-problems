#Two Sum Problem
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

#[2,7,11,15], target=9 
        for i in range(len(nums)): #len = 0,1,2,3 (4) [1st i=0]
            for j in range(i + 1, len(nums)): # j begins from i+1 [j=1]
                if nums[i] + nums[j] == target: #num[i=0]= 2 and num[j=1]= 7 ; if 2+7=9, truee
                    result = [i, j] #[0,1]

        return result