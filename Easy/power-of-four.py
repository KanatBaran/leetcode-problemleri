class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n - 1)) == 0 and len(format(n, 'b')) % 2 == 1

"""
class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        # 2'nin kuvveti mi?
        if (n & (n - 1)) == 0:
            # 4'ün kuvveti için (2^k) biçiminde ve k çift olmalı.
            # 2^k sayısının ikilik uzunluğu k+1'dir; k çift ise uzunluk tektir.
            return (len(format(n, 'b')) % 2) == 1
        return False
"""