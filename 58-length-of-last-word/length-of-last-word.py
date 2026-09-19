class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s) -1,-1,-1):
            if s[i] == " ":
                if length > 0:
                    return length
            else:
                length +=1
        return length


        