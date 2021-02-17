

def fixed_point(nums):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == mid:
            return mid
        elif mid > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(fixed_point( [-10, -5, 3, 4, 7, 9] ))
