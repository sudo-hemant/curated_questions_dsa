

def count_triplets(nums, value):

    count = 0
    nums.sort()

    for i in range(len(nums) - 2):
        low, high = i + 1, len(nums) - 1

        while low < high:
            if nums[i] + nums[low] + nums[high] >= value:
                high -= 1
            else:
                count += high - low
                low += 1

    return count


print(count_triplets( [5, 1, 3, 4, 7], 12 ))
        