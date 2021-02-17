
# MOORE VOTING ALGO

# NOTE: this algortihm gives us candidate for the majority element,
# but here since it ll always contain majority element, we are directly
# returning it instead of counting the no of occurences of the candidate majority

def majority_element(nums):

    curr_max, count = nums[0], 1

    for i in range(1, len(nums)):
        if count == 0:
            count += 1
            curr_max = nums[i]
        elif nums[i] == curr_max:
            count += 1
        else:
            count -= 1

    return curr_max    