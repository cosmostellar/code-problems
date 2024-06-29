# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages = []
        while len(nums) != 0:
            averages.append(self.check_nums(nums))

        minimum_average = 999
        for item in averages:
            if item < minimum_average:
                minimum_average = item

        return minimum_average

    def check_nums(self, nums: list[int]) -> float:
        smallest = 999
        largest = 0

        ptr_l = 0
        ptr_r = len(nums) - 1

        while ptr_l < len(nums) / 2 or ptr_r > len(nums) / 2 - 1:
            if nums[ptr_l] < smallest:
                smallest = nums[ptr_l]
            if nums[ptr_l] > largest:
                largest = nums[ptr_l]

            if nums[ptr_r] < smallest:
                smallest = nums[ptr_r]
            if nums[ptr_r] > largest:
                largest = nums[ptr_r]

            if ptr_l < len(nums) / 2:
                ptr_l += 1
            if ptr_r > len(nums) / 2 - 1:
                ptr_r -= 1

        smallest_found = False
        largest_found = False
        new_nums = []

        for num in nums:
            if num == smallest and not smallest_found:
                smallest_found = True
            elif num == largest and not largest_found:
                largest_found = True
            else:
                new_nums.append(num)

        nums[:] = new_nums

        return (smallest + largest) / 2
