def Solution(arr, size):
    A = 0
    for N in range(size):
        if (arr[N] <= 0):
            arr[N], arr[A] = arr[A], arr[N]
            A += 1 # increment count of non-positive integers 
    return A 
  
  
''' Find the smallest positive missing number 
in an array that contains all positive integers '''
def findMissingPositive(arr, size):
      
    # Mark arr[i] as visited by 
    # making arr[arr[i] - 1] negative. 
    # Note that 1 is subtracted 
    # because index start 
    # from 0 and positive numbers start from 1 
    for N in range(size):
        if (abs(arr[N]) - 1 < size and arr[abs(arr[N]) - 1] > 0):
            arr[abs(arr[N]) - 1] = -arr[abs(arr[N]) - 1]
              
    # Return the first index value at which is positive 
    for N in range(size):
        if (arr[N] > 0):
              
            # 1 is added because indexes start from 0 
            return N + 1
    return size + 1
  
''' Find the smallest positive missing 
number in an array that contains 
both positive and negative integers '''
def findMissing(arr, size):
      
    # First separate positive and negative numbers 
    shift = Solution(arr, size)
      
    # Shift the array and call findMissingPositive for 
    # positive part 
    return findMissingPositive(arr[shift:], size - shift) 
      
# Driver code 
arr = [-1, -3 ]
arr_size = len(arr) 
missing = findMissing(arr, arr_size) 
print(missing)
  
