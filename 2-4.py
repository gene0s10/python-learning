maze = [ ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "@", " ", " ", "K", " ", "#", "#"],
    ["#", " ", "#", "#", "#", " ", " ", "#"],
    ["#", " ", "K", " ", "#", "#", "G", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],]

player_pos_x = 0
player_pos_y = 0

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "@":
            player_pos_y = i
            player_pos_x = j
            break

goal_flag = False
key_flag = False

while True: 
    for i in range(len(maze)): 
        line = "" 
        for j in range(len(maze[i])):
            line += maze[i][j]
        print(line)

    if goal_flag: 
        print("ゴール!!!")
        break

    move = input("移動方向を入力 (u:上, d:下, l:左, r:右, q:終了): ")

    new_pos_x = player_pos_x
    new_pos_y = player_pos_y

    if move == "u": 
        new_pos_y = player_pos_y - 1
    elif move == "d":
        new_pos_y = player_pos_y + 1
    elif move == "r":
        new_pos_x = player_pos_x + 1
    elif move == "l":
        new_pos_x = player_pos_x - 1
    elif move == "q":
        print("終了します。")
        break
    else:
        print("正しいキー入力")
        continue

    if maze[new_pos_y][new_pos_x] == "#":
       print("壁なので進めません！")
       continue

    if maze[new_pos_y][new_pos_x] == "G": 
        goal_flag = True

    if maze[new_pos_y][new_pos_x] == "K":
        key_flag = True
        print("鍵を手に入れる")
        maze[new_pos_y][new_pos_x] = " "
    maze[player_pos_y][player_pos_x]

    maze[player_pos_y][player_pos_x] = " "
    maze[new_pos_y][new_pos_x] = "@"

    player_pos_x = new_pos_x
    player_pos_y = new_pos_y