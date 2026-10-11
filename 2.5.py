def calc():
    a=2
    b=5
    result = a + b
    print(result)

calc()
calc()
calc()


def calc(a):
    b = 5
    result = a + b
    print(result)

calc(2)
calc(10)

result = 0
print(f"グローバル変数: {result}")

def calc(a):
    b = 5
    result = a + b
    print(f"ローカル変数: {result}")

calc(2)
print(f"グローバル変数: {result}")

result = 0
print(f"グローバル変数: {result}")

def calc(a):
    global result
    b = 5
    result = a + b
    print(f"グローバル変数: {result}")

calc(2)
print(f"グローバル変数: {result}") 

N = int(input("Input N:"))

total = 0
for i in range(N + 1):
    total += i

print(total)