# Q: To find missing and duplicate number from an n-array(array of size n containing values from 1 to n)
# Complexity: Time: O(n), Space: O(1)

# Idea: sum of squares of actual, sum of actual, 
# sum of n actual, sum of n

# Issue: Not scalable for multiple missing and duplicates

# assume: missing b, duplicate d
# sum_of_n = a+b+c+d, actual_sum = a+d+c+d
# sum_of_sq = a2+b2+c2+d2, actual_sq_sum = a2+d2+c2+d2
# sq_diff = sum_of_sq - actual_sq_sum = b2 - d2
# diff = sum_of_n - actual_sum = b - d
# sum = sq_diff // diff = b2-d2/b-d = b + d (math formula)
# missing = (sum + diff) // 2 = b
# duplicate = sum - missing = d



def fun(nums):
    n = len(nums)
    sum_of_n = (n * (n+1)) // 2
    sum_of_sq = (n * (n+1) * (2*n + 1)) // 6
    actual_sum = 0
    actual_sq_sum = 0
    # to find actual sum and actual square sum
    for i in nums:
        actual_sum += i
        actual_sq_sum += i*i
    
    sq_diff = abs(sum_of_sq - actual_sq_sum)
    diff = sum_of_n - actual_sum  #negative is needed for exact sum calculation

    sum = sq_diff // abs(diff)
    missing = (sum + diff)//2
    duplicate = sum - missing
    return (missing, duplicate)

# implementation
nums = [1,2,3,1,5]
missing, duplicate = fun(nums)
print(f"Missing: {missing}, Duplicate: {duplicate}")
    
    
