"""
Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:

Input:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}
Output: 9

Your Task :
You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
1 ≤ A[i] ≤ 106
"""

# Approach 1
# A.sort()
# for i in range(1, N+1):
#     if i != A[i-1]:
#         print(i)
#         break
#     else:
#         continue

# Approach 2
total_sum = (N * (N+1))//2 # To get total sum of N natural numbers.
sum_of_give_array = sum(A)
print("Missing number: ",total_sum - sum_of_give_array)
