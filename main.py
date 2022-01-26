field = [['-'] * 3 for _ in range(3)]
def show_field(f):
    print(' 0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))
show_field(field)

i = 11
j = 22
print(str(i) < str(j))

def user_input(f):
    while True:
        place = input('Введите координаты :').split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числф')
            continue
        x, y = map(int, place)
        if not(x >= 0 and y >= 0 and y < 3):
            print('вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

user_input(field)

field = [['-']*3 for _ in range(3)]
count = 0
while True:
    if count == 9:
        print('Ничья')
    if count % 2 == 0:
        user = 'x'
    else:
        user = '0'
    show_field(field)
    x, y = user_input(field)
    field[x][y] = user
    count += 1

def win_v1(f,user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
        check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or \
        check_line(f[2][0], f[1][1], f[0][2], user):
                        return True
    return False
win_v1(field,user)

def win_v2(f,user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

def win_3v(f,user):
    f_list = []
    for i in f:
        f_list += 1
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indeces = ([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indeces.intersection(set(p))) == 3:
            return True
        return False

































































































































































































































