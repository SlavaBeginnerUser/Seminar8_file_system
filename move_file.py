from return_data_file import data_file

def move_data():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    print(data[number_row-1])
    temp = data[number_row-1]
    if nf == 1:
        nf = 2
    else:
        nf = 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{temp}\n')
    print("Данные успешно добавлены!")
    
    