class Solution(object):
    def isMonotonic(self, nums):
        sort = sorted(nums)
        print(sort)
        r = False
        so = sort[::-1]
        print(so)
        if sort==nums:
            r = True
        elif so==nums:
            r = True        
        return r
        