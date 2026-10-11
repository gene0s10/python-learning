Probability=int(input('降水確率'))
if Probability <20:
    print('傘はいらない')
if Probability <70:
    print('折り畳み傘を持つ')

point = int(input('数字'))
for i in range(point):
    print(i)
    if i%15 ==0:
        print('fizzbuzz')
    elif i%3 ==0:
        print('fizz')
    elif i%5 ==0:
        print('buzz')
    else:
        print(i)
    