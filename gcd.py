num1 = int(input("Enter first number: "))           
num2 = int(input("Enter second number: "))          
if num2 > num1:                                     
    (num1,num2) = (num2,num1)
while num1%num2 != 0:                              
    (num1,num2) = (num2,num1%num2)                  
print("The GCD of the numbers is ",num2)
