class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """

        seq_01 = 0
        seq_10 = 0

        for i in range(len(s)):
            
            if i % 2 == 0:
                if s[i] != '0':
                    seq_01 += 1
                if s[i] != '1':
                    seq_10 += 1

            else:
                if s[i] != '1':
                    seq_01 += 1
                of s[i] != '0':
                seq_10 += 1

        return min(seq_01, seq_10)