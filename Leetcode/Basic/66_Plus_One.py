class Solution:
    def plusOne(self, digits):
        carry = 0
        
        carry = int((digits[-1] +1) / 10)
        digits[-1] = (digits[-1] +1) % 10

        for i in range(len(digits)-2, -1, -1):
            new_carry = int((digits[i] + carry) / 10)
            digits[i] = (digits[i] + carry) % 10
            carry = new_carry
        
        if carry:
            digits.insert(0, carry)
                
        
        return digits

print(Solution().plusOne([9]))
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([1,9,9]))
print(Solution().plusOne([4,3,2,1]))