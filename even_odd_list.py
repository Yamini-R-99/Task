es=0
os=0
n=int(input("Enter len"))
a=[]
e=[]
o=[]
for i in range(0,n):
  a.append(int(input()))
for i in a:
  if i%2==0:
    e.append(i)
    es=es+i
  else:
    o.append(i)
    os=i+os
print("Elements in even array")
for i in e:
  print(i)
print("Sum of even array:",es)
print("Elements in odd array")
for i in o:
  print(i)
print("Sum of odd array:",os)
