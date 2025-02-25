#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # Pointer for the last unique element

    for j in range(1, len(nums)):  # Iterate through the array starting from the second element
        if nums[j] != nums[i]:  # Found a new unique element
            i += 1  # Move the pointer for the unique element
            nums[i] = nums[j]  # Update the array with the new unique element

    # Return the number of unique elements
    return i + 1

# Example usage:
nums = [1, 1, 2, 2, 3, 4, 4, 5]
k = remove_duplicates(nums)
print(k)  # Output: 5 (The unique elements are [1, 2, 3, 4, 5])
print(nums[:k])  # Output: [1, 2, 3, 4, 5]
