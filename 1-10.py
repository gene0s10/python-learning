play = int(input('時間を入力:'))
time = int(input('加入期間入力:'))
if play >= 50 and time >=1:
  print('抽選に参加可能')
if play <=50 and time>=1:
  print('抽選に参加可能出来ません')


play = int(input('角度'))
if play >=90<=180:
 print('鈍角')
if play == 90:
  print('直角')
if play >0<90:
  print('鋭角')
else:
  print('対応していない')


test =int(input('点数を入力'))
if test == 100:
  print('大変よくできました')
if test >=60:
  print('よくできました！')
if test <60:
  print('頑張りましょう')
