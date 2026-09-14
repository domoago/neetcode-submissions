class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroInList = 0
        product = 1
        for num in nums:
            if num == 0:
                zeroInList += 1
            else:
                product *= num
        res = []
        for num in nums:
            if num == 0 and zeroInList == 1:
                res.append(product)
            elif num == 0 and zeroInList > 1:
                res.append(0)
            elif zeroInList:
                res.append(0)
            else:
                res.append(product // num)
        return res