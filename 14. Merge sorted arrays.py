# Merge Sorted Array
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1
has a size equal to m + n such that it has enough space to hold additional elements from nums2
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    nums3 = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            nums3.append(nums2[j])
            j += 1
        elif nums1[i] == nums2[j]:
            nums3.append(nums1[i])
            i += 1
            nums3.append(nums2[j])
            j += 1

    while i < m:
        nums3.append(nums1[i])
        i += 1

    while j < n:
        nums3.append(nums2[j])
        j += 1

    for i in range(0, len(nums1)):
        nums1[i] = nums3[i]
    print(nums1)


merge([1,2,3,0,0,0],3,[2,5,6],3)