# Using the HBI (Hypothesis, Base condition, Induction) method

# Reverses the stack
def reverse(stack):
    if(len(stack) <= 1):
        return
    top = stack.pop()
    reverse(stack)
    insert(stack, top)  # a sub-problem

# Inserts a given value to the end of the current stack
def insert(stack, value):
    if(len(stack) == 0):
        stack.append(value)
        return
    top = stack.pop()
    insert(stack, value)
    stack.append(top)

# Implementation
nums = [2,4,5,6,7]
reverse(nums)
print(nums)
    
