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

# def solution(A, K):
#     n = len(A)

#     # if A is empty, return False
#     if n == 0:
#         return False
#     # if K<0, return False
#     if K <= 0:
#         return False

#     # Check whether it matches the pattern 
#     for i in range(n - 1):
#         # if (A[i] + 1 < A[i + 1]):
#         if (A[i] == A[i+1] or A[i]+1 == A[i+1])
#             return False
#     # if (A[0] != 1 and A[n - 1] != K): # the first should be 1 and the last should be K
#     if (A[0] != 1 or A[n-1] != K):
#         return False
#     else:
#         return True


def solution(N):
    # write your code in Python 3.6
    if N < 0 or not isinstance(N, int):
        raise ValueError

    value = 11**N
    string = str(value)
    count = string.count('1')
    print(count)

if __name__ == "__main__":
    # nums1 = [1,3]
    # nums2 = [2]
    # nums3 = [1,2]
    # nums4 = [3,4]
    # result1 = Solution().findMedianSortedArrays(nums1,nums2)
    # result2 = Solution().findMedianSortedArrays(nums3,nums4)
    # print(result1,result2)
    res1 = solution(3)
    print(res1)


