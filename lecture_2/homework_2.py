# Задание №1
a = 4
print(f'Периметр квадрата: {a * 4} \n'
      f'Площадь квадрата: {a ** 2} \n'
      f'Диагональ квадрата: {(a * a + a * a) ** 0.5}')

# Задание №2
a, b, c = 3, 6, 2
if b ** 2 - 4 * a * c > 0:
    print(f'x1 = {round((-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a), 2)} \n'
          f'x2 = {round((-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a), 2)}')
else:
    print('Не подходит')

# Задание №3
string1 = 'сторона квадрата'
string2 = 'которая объединит эти две строки'
print(f'{string1.replace(string1[0:2], string2[0:2])} {string2.replace(string2[0:2], string1[0:2])}')

# Задание №4
path = 'E:\Games\Call of Duty Modern Warfare\Modern Warfare Launcher.exe'
print(path[(path.rfind('\\')) + 1: -4])
print(path[:path.find('\\') - 1])
a = path[path.find('\\') + 1:]
print(a[:a.find('\\')])

# Задание №5
a = 6
b = 9
print(f'a + b = {a + b}\n'
      f'a * b = {a * b}')

# Задание №6
string = "E:\Games\Call of Duty Modern Warfare\Modern Warfare Launcher.exe"
print(string[::2])

# Задание №7
first_string = 'wtf'
second_string = 'brick quzjmpy veldt whangs fox'
indexes = [second_string.find(first_string[0]), second_string.find(first_string[1]),
           second_string.find(first_string[2])]
a = min(indexes)
b = max(indexes)
print(second_string[a:b])
