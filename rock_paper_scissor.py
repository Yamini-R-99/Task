n1=input("Enter rock/scissor/paper:::")
n2=input("Enter rock/scissor/paper:::")
if(n1=="scissor"and n2=="paper"):
  print("Player 1 wins....")
if(n1=="scissor" and n2=="rock"):
  print("playe 2 wins....")
elif(n1=="paper"and n2=="scissor"):
  print("Player 2 wins...")
elif(n1=="rock"and n2=="paper"):
  print("Player 2 wins...")
elif(n1=="paper"and n2=="rock"):
  print("Player 1 wins....")
elif(n1=="rock"and n2=="scissor"):
  print("Player 2 wins...")

