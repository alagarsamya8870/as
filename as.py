fno=int(input())
sno=list(map(int,input().split()))
sno.sort()
print(sno[0],sno[fno-1])
