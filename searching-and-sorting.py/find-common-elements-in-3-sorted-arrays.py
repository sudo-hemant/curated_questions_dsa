

# TODO:     didn't understand how in gfg the comparisons were quite less ? 

def common_element(nums_1, nums_2, nums_3):

    i, j, k = 0, 0, 0
    ans = []

    while i < len(nums_1) and j < len(nums_2) and k < len(nums_3):

        if nums_1[i] == nums_2[j] and nums_2[j] == nums_3[k]:
            ans.append(nums_1[i])
            i, j, k = i + 1, j + 1, k + 1
        elif nums_1[i] <= nums_2[j] and nums_1[i] <= nums_3[k]:
            i += 1
        elif nums_2[j] <= nums_1[i] and nums_2[j] <= nums_3[k]:
            j += 1
        else:
            k += 1

    return ans


print(common_element( 
    [1, 5, 10, 20, 40, 80],
    [6, 7, 20, 80, 100],
    [3, 4, 15, 20, 30, 70, 80, 120]
 ))
