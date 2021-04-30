
n = int(input())


for test in range(n):
    coin1, coin2 = [int(x) for x in input().split()]
    greater = max(coin1,coin2)
    smaller = min(coin1,coin2)
    
    if coin1 + coin2 == 0:
        print("YES")
        continue

    if coin1 == coin2:
        if (coin1+coin2) % 3 == 0:
            print("YES")
        else:
            print("NO")

    elif smaller * 2 < greater:
        print("NO")

    else:
        if (coin1+coin2) % 3 == 0:
            print("YES")
        else:
            print("NO")

   
