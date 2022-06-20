class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        differnce = abs(arr[0] - arr[1])
        
        for i in range(1, len(arr)-1):
            if abs(arr[i] - arr[i+1]) != differnce:
                return False
        
        return True