class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Finding the smaller of the two lists
        if len(nums1) < len(nums2):
            median = self.findMedian(nums1, nums2)
        else:
            median = self.findMedian(nums2, nums1)

        return median

    def findMedian(self, smaller_array: List[int], larger_array: List[int]) -> float:
        # Initiating Variables
        total_length = len(smaller_array) + len(larger_array)
        half = total_length // 2
        left_pointer = 0
        right_pointer = len(smaller_array) - 1

        if total_length % 2 == 0:
            is_even = True
        else:
            is_even = False

        while True:
            # Calculating Midpoints of each array
            middle_smaller_array = (left_pointer + right_pointer) // 2
            middle_larger_array = half - middle_smaller_array - 2
            
            # Setting the indices of where the partitions begin/end to the value or +- infinity
            if middle_smaller_array >= 0:
                smaller_left_partition = smaller_array[middle_smaller_array]
            else:
                smaller_left_partition = -1000001.00

            if (middle_smaller_array + 1) < len(smaller_array):
                smaller_right_partition = smaller_array[middle_smaller_array + 1]
            else:
                smaller_right_partition = 1000001.00

            if (middle_larger_array) >= 0:
                larger_left_partition = larger_array[middle_larger_array]
            else:
                larger_left_partition = -1000001.00

            if (middle_larger_array + 1) < len(larger_array):
                larger_right_partition = larger_array[middle_larger_array + 1]
            else:
                larger_right_partition = 1000001.00

            if smaller_left_partition <= larger_right_partition and larger_left_partition <= smaller_right_partition:
                # The total of both array lengths is odd
                if not is_even:
                    return min(smaller_right_partition, larger_right_partition)

                # The total of both array lengths is even and therefore we need a summed median
                else:
                    return ((max(smaller_left_partition, larger_left_partition) + min(smaller_right_partition, larger_right_partition)) / 2)

            elif smaller_left_partition >= larger_right_partition:
                right_pointer = middle_smaller_array - 1

            else:
                left_pointer = middle_smaller_array + 1

