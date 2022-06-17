class Solution:
    def hammingWeight(self, n: int) -> int:
        strn = bin(n)
        count = strn.count('1')
        return count
        