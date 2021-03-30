#weird algorithm from CSES Problem Set
'''Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a given value of n.

Input

The only input line contains an integer n.

Output

Print a line that contains all values of n during the algorithm.

Constraints

    1≤n≤106


Example

Input:
3

Output:
3 10 5 16 8 4 2 1'''


def weird_algo(n):
    out.append(n)
    if(n==1):
        return None
    if(n%2==0):
        weird_algo(n/2)
    else:
        weird_algo(n*3+1)

if __name__ == "__main__":
    out = []
    import sys
    if len(sys.argv) != 2:
        print("Weird Algorithm needs exactly one integer as input. Calls \"python3 weird_algo.py 3\" for example.")
    else:
        weird_algo(int(sys.argv[1]))
        import matplotlib.pyplot as plt
        print(out)
        plt.bar(x=[i for i in range(len(out))], height=out)
        plt.show()
        