Number=int(input("Enter no:"))
i = 0
f = 0
s = 1
while(i < Number):
           if(i <= 1):
                      n = i
           else:
                      n = f + s
                      f=s
                      s=n
           print(n)
           i = i + 1
