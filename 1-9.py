test = int(input("tennsuu:"))
if test >= 60:
    print('pass')
if test < 60:
    print('fail')


test = int(input("Score:"))
if test >= 60:             
    print("Pass")
else:                      
    print("Fail")


point = int(input("点数:"))
if 90 <= point:
    print("A")
elif 80 <= point:
    print("B")
elif 70 <= point:
    print("C")
elif 60 <= point:
    print("D")
else:
    print("E")

num = int(input("number:"))
if 100 <= num:
    print("100より大きいです")
if 100 == num:
    print("100が入力されました")
if 100 >= num:
    print ("100未満です")