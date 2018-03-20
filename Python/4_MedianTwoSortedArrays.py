class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        joined = sorted (nums1 + nums2)
        if len(joined)%2:
            i = len(joined)//2 
            return joined[i]
        else:
            i1 = len(joined)//2 - 1
            i2 = len(joined)//2
            value = (joined[i1] + joined[i2])/2
            return value

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    nums3 = [1,2]
    nums4 = [3,4]
    result1 = Solution().findMedianSortedArrays(nums1,nums2)
    result2 = Solution().findMedianSortedArrays(nums3,nums4)
    print(result1,result2)

