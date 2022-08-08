class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        num =0
        for sentence in sentences:
            if(sentence.count(' ') + 1 > num):
                num = sentence.count(' ') + 1
                
        return num