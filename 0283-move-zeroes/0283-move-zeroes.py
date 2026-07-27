class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        i=0
        j=0
        n=len(a)
        while(i<=n-1):
            if a[i]==0:
                j=i+1
                break
            else:
                i+=1
        while(i<=n-1 and j<=n-1):
            if a[i]==0 and a[j]!=0:
                a[i],a[j]=a[j],a[i]
                i+=1
                j+=1
            else:
                j+=1

        