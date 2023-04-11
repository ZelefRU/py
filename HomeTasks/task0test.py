from HomeTasks.Functions import *

'''Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

# number = 0
try:
    day = int(input("Input day of week: "))
    number = day
except:
    print(f"Is not number")

while number > 7:
    number -= 7
dayname = DayOfWeek(number)

if number == 6 or number == 7:
    print(f"{dayname} - weekend")
elif number < 1:
    print(f"{number} - not correct")
else:
    print(f"{dayname} - work day")
