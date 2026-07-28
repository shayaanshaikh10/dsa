class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            x=x*-1
            neg=True
        else:
            neg=False
        while(x>0):
            num=x%10
            x=int(x/10)
            rev=rev*10+num
        if rev>2**31 or rev<-2**31:
            return 0
        elif neg:
            return rev*-1
        else:
            return rev

        
        