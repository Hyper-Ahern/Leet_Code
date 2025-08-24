class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = []

        for i in range (len(nums)):
            left_pointer = i+1
            right_pointer = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

                if current_sum == 0:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[left_pointer])
                    temp.append(nums[right_pointer])
                    solution.append(temp)
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1

                elif current_sum > 0:
                    right_pointer -= 1

                elif current_sum < 0:
                    left_pointer += 1

        return solution