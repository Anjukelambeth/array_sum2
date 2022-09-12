from array import array
 
n=int(input('Enter the lenth of array'))
target=int(input('Enter the target'))
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# Solution with time complexity =O(n^2)
def Solution(n,array1,target):
   
    for i in range(0,n):
        for j in range(i+1,n):
            if array1[i]+array1[j]==target:
                return [i,j]

a= Solution(n,arr,target)
print(a)

