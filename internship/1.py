Array = input("Please enter number : ")
Sum   = input("Please enter sum : ")
Sum = int(Sum)
arr = Array.split(' ')
for i in range(0,len(arr)):
    arr[i] = int(arr[i])

usedNum = set()
# print(arr)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        # if(not(i in usedNum)and not (j in usedNum)):
        if(arr[i] + arr[j] == Sum):
                print(arr[i],",",arr[j])