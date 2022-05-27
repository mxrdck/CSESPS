

n = int(input())
weights = [int(x) for x in input().split()]

left = [] 
right = []

half = sum(weights) // 2

while(len(weights)>0):
    weight = weights.pop()

    if sum(left)+weight <= half:
        left.append(weight)
    else:
        right.append(weight)

    
print(abs(sum(left)-sum(right)))