'''
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input

The first input line contains an integer n: the size of the array.

Then, the second line contains n integers x1,x2,…,xn: the contents of the array.

Output

Print the minimum number of moves.

Constraints

    1≤n≤2⋅105


1≤xi≤109


Example

Input:
5
3 2 5 1 7

Output:
5'''

size = int(input())
numbers = [int(x) for x in input().split()]

n = 0
moves = 0 
sum_numbers = sum(numbers)

#make increasing array 
#we want to calc the moves and not perform the actual +1 move
#hence we can increase each number by more than +1 at a time 
while(n < len(numbers)-1):
    i = n+1 

    while(i <= len(numbers)-1):

        if numbers[n] > numbers[i]:
            moves += numbers[n] - numbers[i]
            i +=1 

        else: 
            n = i
            break
    n = i

print(moves)