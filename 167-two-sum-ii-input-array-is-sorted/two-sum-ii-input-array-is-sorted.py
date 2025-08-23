class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers)-1
        solution = []

        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] == target:
                solution.append(left_pointer + 1)
                solution.append(right_pointer + 1)
                return solution
                
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1

            else:
                left_pointer += 1
