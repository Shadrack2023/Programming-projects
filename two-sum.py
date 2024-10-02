
class Solution:

    def twoSum(self, nums, target):

        #This is a Dictionary to store a number and its index
        num_to_index = {}

        #This code will Iterate over the array
        for i, num in enumerate(nums):

            complement = target - num #this will calculate the complement

            # If the complement is found in the dictionary, it will return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Otherwise, store the index of the current number in the dictionary
            num_to_index[num] = i

        # Return an empty list if no solution is found (shouldn't happen based on problem constraints)
        return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
