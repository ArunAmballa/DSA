class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        carry=1
        ind=0
        while carry:
            if ind<len(digits):
                if digits[ind]==9:
                    digits[ind]=0
                else:
                    digits[ind]=digits[ind]+1
                    carry=0
            else:
                digits.append(carry)
                carry=0
            ind=ind+1
        return digits[::-1]

        