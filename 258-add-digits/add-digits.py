class Solution:
    def addDigits(self, num: int) -> int:
        
        # 0 % 9 is 0 so this is an edge case of digital root calculations
        if num == 0:
            return 0
        
        # Because we work in a base 10 system and 231 = 1* 10^0 + 3* 10^1 + 2* 10^2,
        # modding (or dividing essentially) by 9 gives 1* 1^0 + 3* 1^1 + 2* 1^2 otherwise
        # viewed as 1+3+2 as 1^anything = 1. so 231 % 9 is 6 which is 2+3+1
        digital_root = num % 9

        # Therefore, if a 0 is acheived, it means num was a multiple of 9 and the last number
        # must have been a 9 (81 = 8 + 1 mod 9 = 0 but the answer was 8+1 as 9 is a single digit)
        if digital_root == 0:
            return 9
        else:
            return digital_root