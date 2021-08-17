from typing import Text


arr = input("Please Enter array : ")

array = arr.split(' ')
for i in range(0,len(array)):
    array[i] = int(array[i])

def get_result(tmp_arr):
    n = len(tmp_arr)
    # มีค่าตัวเดียวไม่ต่อเนื่อง
    if(n == 1):
        txt = str(tmp_arr[0])
    # ค่าต่อเนื่อง
    elif(n>1):
        txt = str(tmp_arr[0]) + '-' + str(tmp_arr[n-1])
    return txt

tmp_arr = []
tmp_arr.append(array[0])
result = []
for i in range(1,len(array)):
    current = array[i]
    prev = array[i-1]
    #ถ้าไม่ต่อเนื่อง
    if current != prev + 1:
        txt = get_result(tmp_arr)
        result.append(txt)
        #ล้างค่า arr 
        tmp_arr = []
        #แสดงผลลัพธ์
    tmp_arr.append(current)
    #แสดงค่าที่เหลือใน arr
    txt = get_result(tmp_arr)
result.append(txt)
print(result)

