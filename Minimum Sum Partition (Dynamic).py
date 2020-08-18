def msp(arr):
    total = sum(arr) // 2 + 1
    memo = [False] * total
    memo[0] = True
    for i in arr:
   	 for j in range(total - 1, i - 1, -1):
   		 if memo[j - i]:
   			 memo[j] = True
    for j in range(total - 1, -1, -1):
   	 if memo[j]:
   		 return sum(arr) - 2 * j

array = [1,2,2,2,3]
print(msp(array))