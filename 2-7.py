with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("f.write()で書き換えました")

with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)