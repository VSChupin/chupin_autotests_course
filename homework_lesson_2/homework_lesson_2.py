import math

def exercise_1():
    # Дано 1 число - сторона квадрата. Напишите программу, которая рассчитает 3 значения:
    # периметр квадрата, площадь квадрата и диагональ квадрата.

    side_of_the_square = 150 # сторона квадрата

    square = side_of_the_square ** 2 # площадь
    perimeter = side_of_the_square * 4 # периметр
    diagonal = side_of_the_square * math.sqrt(2) # диагональ d = s * корень из 2, где s — сторона квадрата.

    print(f"Если сторона квадрата = {side_of_the_square}, тогда:\n"
          f"площадь = {square}\n"
          f"периметр = {perimeter}\n"
          f"диагональ = {diagonal}"
          )

def exercise_2():
    # Дано квадратное уравнение x^2+bx+c=0.
    # Дискриминант уравнения должен быть больше 0.
    # Напишите программу, которая найдет корни квадратного уравнения и округлит их до 2 знаков после запятой.

    a = 1
    b = 4
    c = 3

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Дискриминант равен {d}\n"
            "Корни уравнения:", round(x1, 2), round(x2, 2))

def exercise_3():
    # Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их пробелом,
    # а также поменяет местами первые два символа первой строки на первые два символа второй строки и наоборот.

    string1 = 'Сердце в будущем живет.'
    string2 = 'Я памятник себе воздвиг нерукотворный.'

    sum_string = string1 + " " + string2
    replaced_string = string1.replace(string1[0:2], string2[0:2])
    replaced_back_string = string2.replace(string2[0:2], string1[0:2])

    print(f"объединение строк и разделение пробелом:\n= {sum_string}\n"
          f"\nзамена местами первые 2 символа первой строки на первые 2 симовола второй строки и наоборот:\n"
          f"= {replaced_string}\n"
          f"наоборот:\n"
          f"= {replaced_back_string}")

def exercise_4():
    # Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.

    abs_path = r"C:\Users\vs.chupin\Downloads\example.xml"
    split_path = abs_path.split("\\")
    filename = split_path[4]
    only_name = filename[:-4]

    print(f"абсолютный путь: {abs_path}"
          f"\nназвание файла без расширения: {only_name}"
          f"\nназвание диска: {(split_path[0])[:-1]}"
          f"\nкорневая папка: {split_path[3]}")

def exercise_5():
    # Дано 2 числа a и b. Используя форматирование строк,
    # выведите на экран их сумму и произведение в форматах ’a + b = c’ и ’a*b = c’.

    a = 4
    b = 3
    c = a + b
    e = a*b
    print(f"{a} + {b} = {c}"
          f"\n{a} * {b} = {e}")

def exercise_6():
    # Дана строка. Напишите программу удаления символов,
    # которые имеют нечетные значения индекса заданной строки.

    string = "В душе моей — сиянье звёзд, Мерцанье их в ночи бездонной."\
             " И свет их, что не гаснет, прост, Как луч надежды, окрылённой."

    formatted_string = ''

    for i, char in enumerate(string):
        if i % 2 == 0:
            formatted_string = formatted_string + char
    print(formatted_string)

def exercise_7():
    # Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа,
    # вторая точно содержит символы первой строки в любом порядке.
    # Напишите программу, не используя циклы и условия, которая находит срез
    # минимальной длины во второй строке, который будет содержать все символы первой строки.
    # Например, first_string = ‘wtf’ и second_string = ‘brick quz jmpy veldt whangs fox’,
    # срез минимальной длины: ‘t whangs f’

    first_string = 'wtf'
    second_string = 'brick quz jmpy veldt whangs fox'

    index_list = []

    index_0 = second_string.find(first_string[0])
    index_list.append(index_0)
    index_1 = second_string.find((first_string[1]))
    index_list.append(index_1)
    index_2 = second_string.find((first_string[2]))
    index_list.append(index_2)

    index_list.sort()

    result = second_string[index_list[0]:index_list[2]+1]
    print(result)


def main():
    print("\n1 упражнение:")
    exercise_1()
    print("\n2 упражнение:")
    exercise_2()
    print("\n3 упражнение:")
    exercise_3()
    print("\n4 упражнение:")
    exercise_4()
    print("\n5 упражнение:")
    exercise_5()
    print("\n6 упражнение:")
    exercise_6()
    print("\n7 упражнение:")
    exercise_7()

main()
