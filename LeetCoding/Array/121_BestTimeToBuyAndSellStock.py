class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10000
        l_max = 0
        for i in prices:
            if i < min:
                min = i
            if l_max < i - min:
                l_max = i - min
        return l_max

'''
Runtime: 916 ms, faster than 98.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.3 MB, less than 11.43% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''