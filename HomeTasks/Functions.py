def Sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

def DayOfWeek(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"
    else:
        return "???"

# определение функции декоратора
def select(input_func):
    def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()  # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки

    return output_func  # возвращаем новую функцию

#
# # определение оригинальной функции
# @select  # применение декоратора select
# def hello():
#     print("Hello METANIT.COM")
#
#
# # вызов оригинальной функции
# hello()