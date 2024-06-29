# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages = []

        while len(nums) != 0:
            averages.append(self.check_nums(nums))

        return min(averages) if averages else 0

    def check_nums(self, nums: list[int]) -> float:
        smallest = min(nums)
        largest = max(nums)

        nums.remove(smallest)
        nums.remove(largest)

        return (smallest + largest) / 2
