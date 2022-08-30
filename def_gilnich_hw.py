# периметр площадь диагональ
# def square(a):
#     return (4*a, a**2, (2*a**2)**.5)
# result = square(int(input("enter сторону квадрата:")))
# print(result)

#високосный год
# def is_year_leap():
#     year = int(input())
#     if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
#         return print(True)
#     else:
#         return print(False)
#
# is_year_leap()

# (зима, весна, лето или осень)
# def season(month):
#     if month in (12, 1 ,2):
#         return "зима"
#     elif month in (3,4, 5):
#         return "весна"
#     elif month in (6, 7, 8):
#         return "лето"
#     elif month in (9, 10, 11):
#         return "осень"
# result = season(int(input("Введите месяц:")))
# print(result)

# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

# def is_prime(x):
#     a = True
#     for i in range(2, int(x**0.9)):
#         if x % i == 0:
#             a = False
#     return(a)
# result = float(input("Enter numder:"))
# print(is_prime(result))


# Функция, вычисляющая среднее арифметическое элементов массива. Массив должен состоять из случайных чисел, длинной 10 элементов.
# import random
# N = 10
# def average(a):
#     s = 0
#     for i in range(N):
#         s += a[i]
#     return s/N
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(random.randint(1,10))
# b = average(arr)
# print(arr)
# print(b)

def calculation():


    choice = input("choice_command")
    a = float(input("Enter: "))
    b = float(input("Enter: "))

    if choice == "+":
        print("{} + {}" .format(a, b))
        print(a + b)

    elif choice == "-":
        print("{} - {}" .format(a, b))
        print(a - b)

    elif choice == "*":
        print("{} * {}" .format(a, b))
        print(a * b)

    elif choice == "/" and b !=0:
        if b == 0:
            print("{} / {}" .format(a, b))
        print(a / b)
    try:
        res = a / b
    except ZeroDivisionError:
        res = 0
    print(res)
calculation()
def again():
    choice_again = input("choice_command")
    if choice_again == "Y":
        calculation()
    elif choice_again == "N":
        print("Exit")
    else:
        again()
        calculation()