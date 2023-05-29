# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

month_input = input("Введите номер месяца: ")

month_dict = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь"} 

def quarter_of(month, month_input):
    if month in [1, 2, 3]:
        return print(f'Месяц {month_input} ({month_dict[month]}) является частью первого квартала')
    elif month in [4, 5, 6]:
        return print(f'Месяц {month_input} ({month_dict[month]}) является частью второго квартала')
    elif month in [7, 8, 9]:
        return print(f'Месяц {month_input} ({month_dict[month]}) является частью третьего квартала')
    elif month in [10, 11, 12]:
        return print(f'Месяц {month_input} ({month_dict[month]}) является частью четвертого квартала')
    else:
        return "Некорректный номер месяца"

quarter_of(int(month_input), month_input)


