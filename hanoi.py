
'''how to hanoi: https://www.mathsisfun.com/games/towerofhanoi.html'''


n = int(input())

print(2**n-1)

def solve_hanoi(n):
    a = [x for x in range(1,n+1)]
    b = []
    c = []
    if n % 2 == 0:
        solved = False
        while(not solved):

            #alternate between smallest and non smallest tile acc to https://en.wikipedia.org/wiki/Tower_of_Hanoi#Binary_solution
            smallest = min(a[0],b[0],c[0])
            #move smallest to the right, non-smallest to the left

            

        
    else:
        play_smallest = True
        while(True):
            #alternate between smallest and non smallest tile acc to https://en.wikipedia.org/wiki/Tower_of_Hanoi#Binary_solution
            
            #move smallest to the left, non-smallest to the right

            #if smallest has to be played
            if play_smallest:
                smallest = min(a[0],b[0],c[0])

                #try to move to left, else move to end of stack
                if a[0] == smallest:
                    a.remove(smallest)
                    if smallest not in c:
                        c.append(smallest)
                    else:
                        b.append(smallest)
                
                if smallest in b:
                    b.remove
