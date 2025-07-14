# LeetCode 128. Longest Consecutive Sequence
# Difficulty: Medium
# Runtime: 48ms, Beats 81.97%/ Memory: 27.05MB, Beats 44.89%

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Return 0 if the list is empty.
        if not nums:
            return 0
        
        num_set = set(nums) #Remove duplicates from the set
        longest = 0

        for num in num_set:
            #If num - 1 does not exist, num is the starting point of the consecutive sequence.
            if num - 1 not in num_set:
                current_num = num
                length = 1
                
                #Check if the following numbers are present
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1
                
                #Update the maximum length
                longest = max(longest, length)

        return longest
        