max=int(input("Enter min range:"))
min=int(input("Enter max range:"))
Sum=0
for j in range(min,max):
    for i in range(1,j):
        if(Number % i == 0):
             Sum = Sum + i
             if (Sum == Number):
                 print(" %d is a Perfect Number" %Number)
             else:
                 print(" %d is not a Perfect Number" %Number)
