

# NOTE: this sol doesn't handle cases where all elements are either negative or 0

def maxProduct(self, arr, n):
    
    max_so_far = float('-inf')
    min_ending_here, max_ending_here = 1, 1
    
    for i in range(n):

        # if the current element is greater than 0, then we know that
        
        # case 1: max_ending_here ll either be 1 or some positive element,
        # so mutliplying it by a +ve no ll give us +ve no only

        # case 2: min_ending here ll either be 1 or -ve element,
            # case 2.a : if it is -ve than multiplying it by +ve no ll give us bigger -ve no
            # case 2 b : if it is 1, than mutliplying it by +ve no ll give us +ve no, so we have
            # to make it 1 in that case

        if arr[i] > 0:
            min_ending_here = min(min_ending_here * arr[i], 1)
            max_ending_here *= arr[i]

        # if curr no is zero, max_product cannot end here 

        elif arr[i] == 0:
            min_ending_here, max_ending_here = 1, 1

        # if the current element is -ve, we know that 
        # multiplying it by +ve no ll give us -ve no
        
        # case 1 : max_ending_here ll always be +ve (1, or greater) so it ll always result in -ve no
        # so we ll multiply it by curr element, and ll store it 
        # in min_ending here

        # case 2 : since max_ending here ll always be +ve and curr element is -ve
        # we can't multiply it with the max_ending_here
        
            # case 2.a : if min_ending_here < 0
            # and if we ll multiply it by -ve element, we ll get a positive element
            
            # case 2.b : if min_ending_here == 1
            # and mutliplying it by -ve element ll make it -ve, so we are not going to include curr ele
        

        elif arr[i] < 0:
            temp = min_ending_here
            min_ending_here = max_ending_here * arr[i]
            max_ending_here = max(temp * arr[i], 1)
        
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far



# -----------------------------------------------------------


# NOTE: this case handles where all elements are either +ve or 0


# When arr[i] is positive : As maxval is maximum possible value, simply multiply arr[i] with maxval to obtain new maxval. 
# minval is minimum possible negative product. If its previous value is negative then simply multiply it with arr[i]. If its value is 1 keep it as 1.

# When arr[i] is 0 : Consider the test case : arr[] = {0, -4, 0, -2}. The maximum product is 0 in this case. To account for
# this case in our algo, update maxval with 0 instead of 1 whenever arr[i] is zero. The product of any number with zero is zero. Consider another test case, arr[] = {0, 1 ,2}.
# If maxval remains zero after current iteration (according to the step described above) and the next element is positive 
# then the result will be zero and not the positive element. To consider that at the end of each iteration check if maxval is zero or not.
# If it is zero set it equal to 1. Update minval with 1 as subarray product with zero as element in it will be zero, which
#  results in loss of minimum possible value. So exclude this zero from subarray by setting minval to 1, i.e., restarting product calculation.

# When arr[i] is negative : new value of maxval is previous minval*arr[i] and new value of minval is previous maxval*arr[i
# ]. Before updating maxval, store its previous value in prevMax to be used to update minval.


def max_product(self, arr, n):
    
    max_so_far = float('-inf')
    min_ending_here, max_ending_here = 1, 1
    
    for i in range(n):

        if arr[i] > 0:
            min_ending_here = min(min_ending_here * arr[i], 1)
            max_ending_here *= arr[i]

         # If current element is zero, maximum  
        # product cannot end at current element.  
        # Update minval with 1 and maxval with 0.  
        # maxval is updated to 0 as in case all  
        # other elements are negative, then  
        # maxval is 0.  

        elif arr[i] == 0:
            min_ending_here, max_ending_here = 1, 0

        # If current element is negative,  
        # then new value of maxval is   
        # minval*arr[i] and new value of minval  
        # is previous maxval*arr[i]. Before  
        # updating maxval, store its previous  
        # value in prevMax to be used to  
        # update minval.  
            
        elif arr[i] < 0:
            temp = min_ending_here
            min_ending_here = max_ending_here * arr[i]

            # min_ending_here is either 1 or < 0 
                # case 1 :  if its less than 0, than *ing it by -ve ll make it +ve

                # case 2 :  if it is 1 than our result ll be -ve
                # to handle this case we have already included a if statement below 
                # which ll set it to 1
            max_ending_here = temp * arr[i]
        
        max_so_far = max(max_so_far, max_ending_here)

        if max_ending_here <= 0:
            max_ending_here = 1

    return max_so_far



# ------------------------------------------------------------------------------------------------

# NOTE: best method

# public int maxProduct(int[] A) {
#     if (A.length == 0) {
#         return 0;
#     }
    
#     int maxherepre = A[0];
#     int minherepre = A[0];
#     int maxsofar = A[0];
#     int maxhere, minhere;
    
#     for (int i = 1; i < A.length; i++) {
#         maxhere = Math.max(Math.max(maxherepre * A[i], minherepre * A[i]), A[i]);
#         minhere = Math.min(Math.min(maxherepre * A[i], minherepre * A[i]), A[i]);
#         maxsofar = Math.max(maxhere, maxsofar);
#         maxherepre = maxhere;
#         minherepre = minhere;
#     }
#     return maxsofar;
# }


# I figure out this solution by thinking that: what we need to know to calculate maximum product at i? 
# Recall what we did in Maximum Subarray Sum (Kadane algorithm), only known maximum ends at i-1 is not enough for this one.

# Due to negative number and property of multiply, we need max and min ends at i-1 in case negative num
# ber at i causes them swap. Therefore, we maintain two local optimal variables, update them in each iteration and the global maximum as well.

# Here is my final solution. Don't forget the third "candidate" num itself as we did in Kadane algorith
# m, since we could discard local optimal value if they are not any more.



