class Solution:

    def removeDuplicates(self, nums):

        if not nums:

            return 0
        
        # Pointer to the last unique element's position
        j = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        
        return j

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    print(f"Number of unique elements: {k}")
    print(f"Array after removing duplicates: {nums[:k]}")
