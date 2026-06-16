class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums) * 2)
        index = 0
        for i in range(2):
            for j in range(len(nums)):
                output[index] = nums[j]
                index += 1
        return output
