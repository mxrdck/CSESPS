'''
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input

The only input line contains an integer n.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints

    1≤n≤106


Example 1

Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6

Example 2

Input:
6

Output:
NO
''' 

#solution: division is possible if the sum of the array is even (sum%2=0). if it is even, because the array is sorted ascending, we can go for greedy approach. 
#loop over the elements and append them to the solution array, until the sum is equal or greater then half of the input array sum. if it is equal, return the created array and the rest of the elemetns 
# if it is greater, remove the first element of the array and put it back to the initial array ,check again. do until desired sum is reached


n = [x for x in range(1,int(input())+1)]
s = sum(n)

if s%2 == 0:
    print("YES")

    half = s/2 

    first = []
    appending = True
    removing = False
    while(appending):

        first.append(n.pop(0))

        if sum(first)==half:
            print(len(first))
            print(*first,sep=" ")
            print(len(n))
            print(*n,sep=" ")
        
        if sum(first)>half:
            appending = False
            removing = True
    
    while(removing):
        n.insert(0, first.pop(0))
        
        if(sum(first)==half):
            print(len(first))
            print(*first,sep=" ")
            print(len(n))
            print(*n,sep=" ")
            removing = False
else:
    print("NO")



