# Запись строки в переменную
example = 'Топинамбур'

# Вывод первого символа
print(example[0])  # Вывод: Т

# Вывод последнего символа (используя отрицательный индекс)
print(example[-1])  # Вывод: р

# Вывод второй половины строки (если строка нечётная, то начиная с середины + 1)
half_index = len(example) // 2 + len(example) % 2
print(example[half_index:])  # Вывод: амбур

# Вывод строки наоборот
print(example[::-1])  # Вывод: рубманипоТ

# Вывод каждого второго символа
print(example[1::2])  # Вывод: оиабр
