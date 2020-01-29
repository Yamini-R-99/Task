s=0
i=0
j=0
print("Enter min range:")
m=int(input())
print("Enter max range:")
n=int(input())
for i in range(m,n):
  for j in range(2,i):
    if i%j==0:
      break
  else:
     print(i)
     s=s+i
print(s)
