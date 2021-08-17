str1 = input("Enter the sentence : ")
words = str1.split()
rev_str1 = []
for i in words:
    rev_str1.append(i[::-1])

sen = " ".join(rev_str1)
print(sen)