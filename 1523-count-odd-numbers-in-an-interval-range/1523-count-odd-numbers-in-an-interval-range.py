class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1) %2 ==0:
            return int((high - low + 1) /2)
        else:
            if high %2 ==0:
                return int((high - low) /2)
            else:
                 return int(((high - low) /2) +1)