from random import random
N = 8
M = 5
arr = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(int(random() * 150))
    arr.append(lst)
for i in range(N):
    for j in range(M):
        print(" |%3d| " % arr[i][j], end='')
    print()
for i in range(M):
    print(" ----- ", end='')
print()
s=[]
for j in range(M):
    mx = arr[0][j]
    for i in range(N):
        if arr[i][j] > mx:
            mx = arr[i][j]
            s.append(mx)
    print(" |%3d| " % mx, end='')
print()
q=0
def ma():
    global q
    q=max(s)
ma()    

print("Максимальный элемент", q)
