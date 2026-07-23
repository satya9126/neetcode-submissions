class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        z=nums.count(0)
        res=[]
        tp = 1
        if z > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
                tp*=num
        for num in nums:
            if z == 1:
                if num == 0:
                    res.append(tp)
                else:
                    res.append(0)
            else:
                res.append(tp//num)
        return res
            
            
        