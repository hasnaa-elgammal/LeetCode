class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strlist =[]
        for i in range(n):
            if (i+1)%3 ==0 and (i+1)%5 ==0:
                strlist.append('FizzBuzz')
            elif (i+1)%3 ==0:
                strlist.append('Fizz')
            elif (i+1)%5 ==0:
                strlist.append('Buzz')
            else:
                strlist.append(str(i+1))
        
        return strlist
        