dict={1:'Micro-20/km',2:'Mini-25/km',3:'Prime-30/km'}
def taxing(s,d,c):
  v=d-s
  tot=c*v
  return tot
def micro():  
  return 20
def mini():
  return 25
def Prime():
  return 30
c=1
ch='y'
while(ch=='y'):
    c=1
    for i,j in dict.items():
      print(i,":",j)
      c=c+1
    s=int(input("select option:"))
    while s>3:
      print("Invalid option")
      s=int(input("select option:"))
    src=int(input("Enter source:"))
    while(src<1):
      print("Invalid source")
      src=int(input("Enter source:"))
    dest=int(input("Enter destination:"))
    while(dest<src):
      print("Enter destination greater than source")
      dest=int(input("Enter destination:"))
    name=input("Enter name::")
    pno=input("Enter pno::")
    if(s==1):
      tot=taxing(src,dest,micro())
    if(s==2):
      tot=taxing(src,dest,mini())
    if(s==3):
      tot=taxing(src,dest,Prime())
    print("Want to print receipt??y/n")
    ch=input()
    if(ch=='y'):
      print("_______Receipt_______")
      print("")
      print("Name::"+name)
      print("Phone number::"+pno)
    print("Total::",tot)
    print("Do u wanna continue??y/n")
    ch=input()


