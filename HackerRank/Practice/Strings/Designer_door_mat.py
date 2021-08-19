import math
n,m = map(int, input().split())
n_mid = math.ceil(n/2)
m_mid = math.ceil(m/2)
for i in range(1,n+1):
    for j in range(1,m+1):
        # print(f'n => {i} m => {j}',end="")
        if n_mid == i:
            if m_mid == j:
                print("WELCOME")
            else:
                print("*",end="")
        else:
            print('-',end="")
        # print(i," ",j," ", end="")

    print()
