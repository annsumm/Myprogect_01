# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
track_1 = random.choice(my_favorite_songs)
track_2 = random.choice(my_favorite_songs)
track_3 = random.choice(my_favorite_songs)

time = track_1[1], track_2[1], track_3[1]

total_time = 0
for i in time:
    total_time += i
print (f'Время звучания трех случайных песен - {round(total_time,2)}')







# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

trackList = list(my_favorite_songs_dict.values())
time = random.choices(trackList, k=3)
total_time = 0
for i in time:
    total_time += i
print (f'Вывод: Три песни звучат {total_time} минут')





