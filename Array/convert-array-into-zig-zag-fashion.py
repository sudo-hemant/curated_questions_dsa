
def zigZag(self,arr, n):
	
	for i in range(len(arr) - 1):
	    
        if not i % 2 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

	    elif i % 2 and arr[i] < arr[i + 1]:
	        arr[i], arr[i + 1] = arr[i + 1], arr[i]
		
