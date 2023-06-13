# def my_pow(number):
#     sum = 0
#     ind = 1
#     for i in str(number):
#         sum += int(i) ** ind
#         ind += 1
#     return sum
#
# print(my_pow(139))

# def my_pow(number):
#     return sum(int(digit) ** (i + 1) for i, digit in enumerate(str(number)))
#
# print(my_pow(139))
#
# def count_args(*args):
#     return len(args)

# 1. Алгоритм линейного поиска

# def search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1
#
# arr = [2, 3, 4, 10, 40] # список может быть в любом порядке
# x = 50
# result = search(arr, x)
# if result == -1:
#     print("Элемент не найден")
# else:
#     print("Индекс элемента равен = ", result)

# 2. Двоичный поиск - поиск в отсортированном массиве путем многократного деления интервала пополам

# def binary_search(arr, low, high, x):
#
#     if high >= low:
#
#         mid = (high + low) // 2
#
#         if arr[mid] == x:
#             return mid
#
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#
#         else:
#             return binary_search(arr, mid + 1, high, x)
#
#     else:
#
#         return -1
#
#
#
# arr = [2, 3, 4, 10, 40] # список должен быть отсортирован
# x = 10
#
#
# result = binary_search(arr, 0, len(arr) - 1, x)
#
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")

# Есть встроенный метод
# print(arr.index(10))

# 3. Сортировка выбором

# Алгоритм сортировки выбором сортирует массив, многократно
# находя минимальный элемент (учитывая возрастающий порядок) из
# неотсортированной части и помещая его в начало. Алгоритм
# поддерживает два подмассива в данном массиве.
#  1) Подмассив, который уже отсортирован.
#  2) Оставшийся несортированный подмассив.
# arr = [ 64 25 12 22 11]
# // Находим минимальный элемент в arr и поместим в начало
# 11 25 12 22 64
# // Находим минимальный элемент в arr и поместим в начало
# 11 12 25 22 64
# // Находим минимальный элемент в arr и поместим в начало
# 11 12 22 25 64
# // Находим минимальный элемент в arr и поместим в начало
# 11 12 22 25 64

# a = [64, 25, 12, 22, 11]
#
# for i in range(len(a)):
#     min_ind = i
#
#     for j in range(i + 1, len(a)):
#         if a[min_ind] > a[j]:
#             min_ind = j
#
#     a[i], a[min_ind] = a[min_ind], a[i]
#
# print(a)

# 4. Пузырьковая сортировка
# 5 1 4 2 8
# Пузырьковая сортировка - это простейший алгоритм сортировки,
# который работает, многократно меняя местами соседние элементы,
# если они находятся в неправильном порядке.
# Первый проход:
# ( 5 1 4 2 8) -> ( 1 5 4 2 8)
# (1 5 4 2 8) -> (1 4 5 2 8), поменять местами с 5> 4
# (1 4 5 2 8) -> (1 4 2 5 8), поменять местами с 5> 2
# (1 4 2 5 8 ) -> (1 4 2 5 8 )ъ
#
# 1 4 2 5 8
# Второй проход:
# ( 1 4 2 5 8) -> ( 1 4 2 5 8)
# (1 4 2 5 8) -> (1 2 4 5 8), поменять местами, поскольку 4> 2
# (1 2 4 5 8) -> (1 2 4 5 8)
# (1 2 4 5 8 ) -> (1 2 4 5 8 )
#
# 1 2 4 5 8
# Третий проход:
# ( 1 2 4 5 8) -> ( 1 2 4 5 8)
# (1 2 4 5 8) -> (1 2 4 5 8)
# (1 2 4 5 8) -> (1 2 4 5 8 )
# (1 2 4 5 8 ) -> (1 2 4 5 8 )

# arr = [64, 43, 25, 12, 22, 11, 90]
#
#
# def bubble_search(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in (range(0, n - i - 1)):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr
#
# print(bubble_search(arr))

# 5. Алгоритм сортировки вставкой

arr = [64, 43, 25, 12, 22, 11, 90]
def insertion_search(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_search(arr))
#
arr = [64, 43, 25, 12, 22, 11, 90]
print(sorted(arr))


arr = list(map(int, input().split()))
arr = [64, 43, 25, 12, 22, 11, 90]
arr = [1, 2, 3, 4, 5, 8, 7]
def IsAscendingTwo(arr):
    for i in range(len(arr) - 1):
        if arr[i+1] < arr[i]:
            return "Нет такого элмента"
    return "Есть такой элемент"

print(IsAscendingTwo(arr))
