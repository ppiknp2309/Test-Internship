n = int(input("input : "))
num = 1
# for i in range(num):
#      print(" ",end="")
for row in range(1,n+1):
    num_space = n-row
    space = ' '*num_space
    content = " "
    for col in range(1,row+1):
        content = content + str(num) + ' '
        num = (num+1)%10
    row_content = space + content
    print(row_content) 