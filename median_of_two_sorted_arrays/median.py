class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        for i in nums1:
            nums2.insert(bsearch(nums2, i), i)
        return nums2[(m + n) // 2] if (m + n) % 2 == 1 else (nums2[(m + n) // 2] + nums2[(m + n) // 2 - 1]) / 2


# log(higher-lower)
def bsearch(array, x, lower=None, higher=None):
    if lower is None:
        lower = 0
    if lower < 0:
        raise ValueError
    if higher is None:
        higher = len(array)
    while lower < higher:
        middle = (lower + higher) // 2
        if array[middle] < x:
            lower = middle + 1
        else:
            higher = middle
    return lower
