class Solution(object):
    def fourSumCount(self, A, B, C, D):
        values = {}
        for num1 in A:
            for num2 in B:
                sum = num1 + num2
                if sum in values:
                    values[sum] += 1
                else:
                    values[sum] = 1

        count = 0
        for num1 in C:
            for num2 in D:
                sum = num1 + num2
                neg = -sum
                if neg in values:
                    count += values[sum]
        return count

A = [50, 1,2]
B = [3, -2,-1]
C = [6, -1,2]
D = [8, 0, 2]

print(Solution().fourSumCount(A, B, C, D))