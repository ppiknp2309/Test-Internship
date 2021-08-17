num = int(input("input : "))
for i in range(num,0,-1):
   for j in range(i,num):
       print(" ",end="")
   for k in range(1,(2*i-1)+1):
       print("*",end="")
   print()
  