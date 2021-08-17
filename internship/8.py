price = int(input("Input : "))
totalMoney = 1000
change = (totalMoney - price)

print(("จำนวนเงินทอน = "),change)
fivebill = change // 500
change = change % 500
onebill = change //100
change = change % 100
fifbill = change // 50
change = change % 50
twenty = change //20
change = change % 20
tencoin = change //10
change = change%10
fivecoin = change // 5
change = change % 5
onecoin = change //1
change = change % 1

print("ธนบัตร 500 ",fivebill,"ใบ")
print("ธนบัตร 100 ",onebill,"ใบ")
print("ธนบัตร 50 ",fifbill,"ใบ")
print("ธนบัตร 20 ",twenty,"ใบ")
print("เหรียญ 10 ",tencoin,"เหรียญ")
print("เหรียญ 5 ",fivecoin,"เหรียญ")
print("เหรียญ 1 ",onecoin,"เหรียญ")