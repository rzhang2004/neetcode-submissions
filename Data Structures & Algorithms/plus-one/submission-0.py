class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1] # reverse
        carry = 1
        for i in range(len(digits)):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        
        if carry == 1:
            digits.append(1)
        
        return digits[::-1]
