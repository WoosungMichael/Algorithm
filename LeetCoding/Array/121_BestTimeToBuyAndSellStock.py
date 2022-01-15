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
Runtime: 900 ms, faster than 99.68% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 55.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''