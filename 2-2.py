correct_number =43

print('kazuate')
while True:
    user_input = input('suuzi:')
    number = int(user_input)
    if number == correct_number: 
        print('せいかい')
        break
    elif number > correct_number:
        print('正解より大きい')
    elif number < correct_number:
        print('正解より小さい')

        print('ゲーム終了')






