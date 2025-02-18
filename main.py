from script import *

def main():

    result_first_action = first_action()
    print(f"Результат first_action: {result_first_action}")

    min_list, max_list, sorted_list = second_action()
    print(f"Минимальный по модулю элемент списка: {min_list}")
    print(f"Максимальный по модулю элемент списка: {max_list}")
    print(f"Отсортированный список по модулю: {sorted_list}")

    original_numbers, updated_numbers = third_action()
    if isinstance(original_numbers, str):
        print(original_numbers)
    else:
        print(f"Введенный список значений: {original_numbers}")
        print(f"Обновленный список: {updated_numbers}")

    result_sum1, result_sum2 = four_action()
    print(f"Результат sum_1 с n=5: {result_sum1}")
    print(f"Результат sum_2 с n=3 и m=4: {result_sum2}")

    N = 4
    M = 5
    matrix = print_matrix(N, M)
    print("Сгенерированная матрица:")
    for row in matrix:
        print(" ".join("{:>3}".format(num) for num in row))

    date_info = display_date_info()
    print(f"Сегодняшняя дата: {date_info['current_date']}")
    print(f"Текущее время: {date_info['current_time']}")
    print(f"Номер дня недели: {date_info['day_of_week']}")
    print(f"Количество дней до 1 июня 2025 года: {date_info['days_until_target']}")


if __name__ == '__main__':
    main()
