import random
from datetime import datetime

def first_action():
    original = 'Pyth1abch2hon'

    first_index = original.find('h')
    last_index = original.rfind('h')

    before_h = original[:first_index + 1]
    between_h = original[first_index + 1:last_index]
    after_h = original[last_index:]

    reversed_between_h = between_h[::-1]

    result = before_h + reversed_between_h + after_h
    return result

def second_action():
    lst = [10, -7, -100, -50, 32, 87, 117, -210]
    min_list = min(lst, key=abs)
    max_list = max(lst, key=abs)
    sorted_list = sorted(lst, key=abs)
    return min_list, max_list, sorted_list

def third_action():
    size = int(input("Введите размер списка: "))

    numbers = []
    print(f"Введите {size} целых чисел:")
    for i in range(size):
        num = int(input(f"Элемент {i + 1}: "))
        numbers.append(num)

    if size < 1:
        return "Список пуст."
    elif size == 1:
        return "Список содержит только один элемент, менять местами нечего."
    else:
        original_numbers = numbers.copy()
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        return original_numbers, numbers

def sum_1(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += 1 / (i ** 2)
    return total_sum

def sum_2(n, m):
    total_sum = 0
    for i in range(1, m + 1):
        total_sum += i * n
    return total_sum

def select_operation(operation, n, m=None):
    if operation == 1:
        return sum_1(n)
    elif operation == 2:
        return sum_2(n, m)
    else:
        return None

def four_action():
    n1 = 5
    n2 = 3
    m = 4

    result_1 = select_operation(1, n1)
    result_2 = select_operation(2, n2, m)

    return result_1, result_2

def print_matrix(N, M):
    matrix = [[random.randint(20, 80) for _ in range(M)] for _ in range(N)]
    return matrix

def display_date_info():
    today = datetime.now()
    day_of_week = today.weekday()
    target_date = datetime(2025, 6, 1)
    days_until_target = (target_date - today).days

    date_info = {
        "current_date": today.strftime('%Y-%m-%d'),
        "current_time": today.strftime('%H:%M:%S'),
        "day_of_week": day_of_week,
        "days_until_target": days_until_target
    }
    return date_info
