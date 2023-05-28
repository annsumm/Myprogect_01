# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

for ind, item in enumerate(my_favorite_songs):
    print (ind,item)

print(f'Первый трек - {my_favorite_songs[0:13]}')
print(f'Последний трек - {my_favorite_songs[63:76]}')
print(f'Второй трек - {my_favorite_songs[15:29]}')
print(f'Второй с конца трек - {my_favorite_songs[50:62]}')
