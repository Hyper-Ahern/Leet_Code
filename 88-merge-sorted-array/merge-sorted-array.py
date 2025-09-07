class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # insert all the elements of nums2 into nums 1 where the zeroes are. Once
        # the counter is higher than nums2 length, stop the loop
        counter = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[counter]
                counter += 1
            if counter >= n:
                break
        
        # Sort in place with python's built in Timsort function
        nums1.sort()