'''
Question link: https://leetcode.com/problems/self-dividing-numbers/

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            temp = num
            isValid = True
            while temp > 0:
                div = temp % 10
                if div == 0 or num % div != 0:
                    isValid = False
                    break
                temp //= 10
            if isValid:
                result.append(num)
        return result
                
