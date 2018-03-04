class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=[]
        for i in list(enumerate(nums)):
            for j in temp:
                if i[1] + j[1] == target:
                    return [j[0],i[0]]
            temp.append(i)
        return []


# Time complexity: O(n), Space complexity: O(n)
    def twoSum2(self, nums, target):
        lookup = {}
        for index, value in enumerate(nums):
            if (target - value) in lookup:
                return [lookup[target-value],index]
            lookup[value] = index
        return []

if __name__=="__main__":
    nums1 = [2,7,11,15]
    target1 = 9
    nums2 = [3,3]
    target2 = 6
    result1 = Solution().twoSum(nums1,target1)
    result2 = Solution().twoSum(nums2,target2)
    print(result1,result2)