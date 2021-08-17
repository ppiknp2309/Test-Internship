
time = float(input("Input : "))
hour = time // 3600
time %= 3600
min = time // 60
time %= 60
sec = time
print(" %02d : %02d : %02d " % (hour,min,sec))