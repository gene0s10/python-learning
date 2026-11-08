file_path = 'todolist.txt'

while True:
    operation = input("何をしますか？（r: 今日やることを見る, a: やることを書き足す, f: 終了）")
    if operation == 'r':
        print("【現在のやるべきことの内容】")
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                print(line, end="")
    elif operation == 'a':
        print("【新しいやることを追加】")
        date = input("日付を入力（例: 2025-06-29）: ")
        entry = input("内容を入力してください: ")
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"{date}: {entry}\n")
    elif operation == 'f':
        break
    else:
        print("無効な入力です")
        continue

print("やることを書く操作を終了しました")













