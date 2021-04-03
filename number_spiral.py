'''
A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints

    1≤t≤105


1≤y,x≤109


Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15'''


def get_spiral_number(row,col):
    z = max(row,col)


    if z % 2 == 0:

        if z == row:
            return z*z-col+1
        else:
            min_val = z*z-(z+(z-2))
            return min_val + (row-1)
    else:
        if z == row:
            min_val = z*z-(z+(z-2))
            return min_val + (col-1)
        else:
            return z*z -(row-1)



t = int(input())

for test in range(t):
    row, col = [int(x) for x in input().split()]
    print(get_spiral_number(row,col))
