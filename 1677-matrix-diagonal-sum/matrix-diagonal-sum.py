class Solution(object):
    def diagonalSum(self, mat):
        f=0
        l=len(mat[0])-1
        s=0
        for i in mat:
            if f==l:
                s+=i[f]
            else:
                s+=i[f]+i[l]
            f+=1
            l-=1
        return s


        
        