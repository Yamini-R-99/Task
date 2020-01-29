s=0
print("Enter min range:")
m=int(input())
print("Enter max range")
n=int(input())
for i in range(m,n):
  if i%2==0:
    s=int(s+i)
print(s)
