# # Create
# a = 'привет'
# b = "привет"
# c = "я 'знаю' Python"
# d = 'я "знаю" Python'
# e = 'я "знаю' Python"
# a = 123
# a = str(a)
# str([1, 1.1, 'a'])
# str(True)
# str(None)
# a = 'привет'
# b = 'Иван'
# c = f"{a} я{b}"
# # Retrive(Read)
# a = 'привет'
# print(a)
# print('Иван')
# a = 'привет'
# a[0]
# a[1]
# a[2]
# a[3]
# a[4]
# a[5]
# a[6]
# a[-1]
# a[-2]
# a[-3]
# a[-4]
# a[-5]
# a[-6]
# a[-7]
# # Update
# a = 'привет'
# a[0] = 'б'
# a = 'бривет'
# # Delete
# a = 'привет'
# del a[0]
# del a
# # Действия со строками
# a = 'привет'
# b = 'Мир'
# c = a + b
# print(c)
# c += b
# a = 'привет'
# b = 2
# c = a * b
# print(c)
# a *= b
# a = "
# b = ""
# c = str()
# # Поисковые методы строк
# help(str)
# a = 'привет мир'
# a.count('р')
# a.find('вет')
# a.index('вет')
# a.rfind('р')
# a.rindex('р')
# # Трансформирующие методы строк
# a = 'привет Мир'
# a.removeprefix('пр')
# a.removesuffix('ир')
print(f'задача№1')
length = 90
wide = 50
perimeter = (90+50)*2
print(perimeter)
print(f'задача№2')
money = 10000
add = 5000
money += add
print(money)
print(f'задача№3')
hours = 5000
days = 5000 // 24
print(days)
hours = 5000 % 24
print(hours)
print(f'задача№4')
diskette_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
diskette_bytes = diskette_mb * 1024 * 1024
chars_per_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = chars_per_book * bytes_per_char
books_on_diskette = int(diskette_bytes // book_size_bytes)
print("На дискету помещается книг:", books_on_diskette)
print(f'задача№5')
pi = 3.1415
radius = 5
side = 5
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
area_square = side ** 2
area_circle = round(area_circle, 2)
circumference = round(circumference, 2)
area_square = round(area_square, 2)
print("Площадь круга:", area_circle)
print("Длина окружности:", circumference)
print("Площадь квадрата:", area_square)

