a=int(input())
x=list(map(int,input().split()))
x.sort()
b=(x[0]+x[a-1])//2
print(b)

