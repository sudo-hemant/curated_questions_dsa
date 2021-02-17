
def majority_element(nums):

    if len(nums) == 1:
        return nums[0]

# here we are taking our 2 majority elements as two random different elements
# bcos we don't know at what places we can find two different values
# for ex if we ll take nums[0], num[1] it ll create problem in [1, 1, ...]
# case 1: if both the elements 0, 1 is not present in whole list, our program ll handle 
# that case too bcos if no match is found, we make curr ele as new majority
# case 2: if both count become 0 at same time, still that case ll be handled bcos 
# whenever we encounter a count 0 we make curr ele as majority but since we don't want a number to be 
# assigned as maj_1 and maj_2 both, we hv put 2 elif conditions so it ll only go inside any of the two 

    majority_1, majority_2 = 0, 1
    count_1, count_2 = 0, 0

    for i in range(len(nums)):
        if nums[i] == majority_1:
            count_1 += 1
        elif nums[i] == majority_2:
            count_2 += 1
        elif count_1 == 0:
            majority_1, count_1 = nums[i], 1
        elif count_2 == 0:
            majority_2, count_2 = nums[i], 1
        else:
            count_1, count_2 = count_1 - 1, count_2 - 1

    majority_count_1, majority_count_2 = 0, 0

    for ele in nums:
        if ele == majority_1:
            majority_count_1 += 1
        elif ele == majority_2:
            majority_count_2 += 1
    
    ans = []
    if majority_count_1 > len(nums) // 3:
        ans.append(majority_1)
    if majority_count_2 > len(nums) // 3:
        ans.append(majority_2)

    return ans

print(majority_element( [1,2] ))