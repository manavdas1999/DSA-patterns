# Q: find missing and duplicate values from n-array(n sized array of values 1-n)

# Complexity: Time: O(n), Space: O(1)

# Idea: As the given array is n-array, we can use swap sort to swap values to their correctIndex

# Highly scalable: works for multiple missing and duplicates

def fun(nums):
    missing = []
    duplicate = []
    i = 0
    while i < len(nums):
        correctIndex = nums[i]-1
        # if correctIndex is already occupied with correct value then we have found the missing and duplicate
        if(nums[correctIndex] == nums[i]):
            i+=1
        else:
            # swap
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        
    for i in range(len(nums)):
        if(nums[i] != i+1):
            # discrepency found
            missing.append(i+1)
            duplicate.append(nums[i])
    
    return (missing, duplicate)

# implementation
nums = [3,3,3,3,3]
missing, duplicate = fun(nums)
print(f"Missing:{missing}, Duplicate: {duplicate}")
