# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что
# задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


def read_last(lines):
    if lines > 0:
        with open('article.txt', 'r', encoding='utf-8') as f:
            file_lines = f.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Количество строк может быть только целым положительным')

lines = int(input('Введите количество строк: '))
read_last(lines)


# 2. Документ «article.txt» содержит следующий текст:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).


def longest_word(filename):
    with open(filename, 'r',encoding='utf-8') as f:
              words = f.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(' '.join(longest_word('article.txt')))



# 3. ДОП ЗАДАЧА.
#
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной
# данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
# Сколько минут на это потребуется? Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt
#
# Пример
# Ввод
#
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273

N = int(input('Введите количество труб: '))
sum=0
A=[0]*N
T=[]
for i in range(N):
    i = str(i + 1)
    print("Введите время трубы номер " + i, end = " ")
    i = int(i)
    i = i - 1
    A[i] = int(input())
L=map(str,list(A))
with open('pipes.txt', 'w',encoding='utf-8') as f:
    for s in L:
        f.write(s+'\n')
    f.write('\n')
    for i in range(1,N+1):
        f.write(str(i)+' ')
with open('pipes.txt', 'r', encoding='utf-8') as f:
    for i in range(N):
        T.append(f.readline().strip())
for el in T:
    sum=sum+1/float(el)
with open('time.txt', 'w',encoding='utf-8') as file:
    file.write(str(1/sum*60))
