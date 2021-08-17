print("Input : ")
nums = list(map(int, input().split()))

def sorteNum(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            nums.sort()
    print(nums)

print("After sorting :")
sorteNum(nums)