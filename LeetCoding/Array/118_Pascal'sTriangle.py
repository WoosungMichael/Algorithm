class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            arr = [[1]]
        elif numRows == 2:
            arr = [[1], [1, 1]]
        else:
            arr = [[1], [1, 1]]
            for i in range(1, numRows - 1):
                tmp = [1]
                for j in range(len(arr[i]) - 1):
                    tmp.append(arr[i][j] + arr[i][j + 1])
                tmp.append(1)
                arr.append(tmp)
        return arr

'''
Runtime: 28 ms, faster than 91.20% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 96.37% of Python3 online submissions for Pascal's Triangle.
'''