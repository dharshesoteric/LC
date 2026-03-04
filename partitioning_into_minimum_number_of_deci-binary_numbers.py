class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        n = str(n)
        num_list = [int(i) for i in n]
        max_num = max(num_list)
        return max_num