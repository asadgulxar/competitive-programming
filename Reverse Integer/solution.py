# Problem Link: https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        maxrange = pow(2,31)-1
        minrange = pow(-2,31)
        isNeg= False
        if x < 0:
            x=x*-1
            isNeg=True
        stringNumber = str(x)
        reverse=''
        for i in range(0,len(stringNumber)):
            reverse = stringNumber[i]+reverse
        try:
            if(isNeg):
                reverse ='-'+reverse
            num=int(reverse)
            if maxrange >= num >=minrange:
                return int(reverse)
            return 0
        except:
            return 0