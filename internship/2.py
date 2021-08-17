from typing import Text


s1 = input("Please enter s1 : " )
s2 = input("Please enter s2 : " )

dict_s1 = dict()
dict_s2 = dict()
for i in range(len(s1)):
    ch1 = s1[i].lower()
    if ch1 in dict_s1:
        dict_s1[ch1] +=1
    else:
        dict_s1[ch1] = 1
for i in range(len(s2)):
    ch2 = s2[i].lower()
    if ch2 in dict_s2:
        dict_s2[ch2] +=1
    else:
        dict_s2[ch2] = 1
if(dict_s1 == dict_s2):
    result = "true"
else:
    result = "false"
print("s1 = ",s1)
print("s2 = ",s2)
print("result")
print(result)
