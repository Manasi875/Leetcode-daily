class Solution:
    def arraySign(self, a):
        cnt = 0

        for num in a:
            if num == 0:
                return 0

            if num < 0:
                cnt += 1

        return -1 if cnt % 2 else 1