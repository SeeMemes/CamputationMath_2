# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

def func1(x3, x2, x1, k, a, b, eps):
    if (func1_check(x3,x2,x1,k,a,b)):
        return 0
    c=0
    x=0
    n = 0
    count = 0
    answer = ''
    while abs(a - b) > eps:
        c = (a + b) / 2
        n += 1
        if f(a, x3, x2, x1, k) * f(c, x3, x2, x1, k) <= 0:
            b = c
        else:
            a = c
            x = (a + b) / 2
        count+=1
        answer += str(count) + '. n = ' + str(n) + '; a = ' + str(a) + '; b =' + str(b) + '; x = ' + str(
            x) + '; f(a) = ' + str(f(a, x3, x2, x1, k)) + '; f(b) = ' + str(f(b, x3, x2, x1, k)) + '; f(x) = ' + str(
            f(c, x3, x2, x1, k)) + '; abs(a-b) = ' + str(abs(a - b)) + '\n'

    answer += 'x = ' + str(x) + ' f(x) = ' + str(f(x, x3, x2, x1, k)) + ' n = ' + str(n) + '\n'
    return answer

def func1_check(x3, x2, x1, k, a, b):
    return f(a,x3,x2,x1,k)*f(b,x3,x2,x1,k)>0

def func3(x3, x2, x1, k, end, eps):
    answer = ''

    if (f(a,x3,x2,x1,k)*f2(a,x3,x2)>0):
        end = a
    else:
        end = b

    count = 0
    tmp_1 = end
    tmp = tmp_1
    tmp_2 = tmp_1 - (f(tmp_1, x3, x2, x1, k) / f1(tmp_1, x3, x2, x1))
    answer += str(count) + '. ' + 'xi-1 = ' + str(tmp_1) + '; xi = ' + str(tmp_2) + '; \n'

    while abs(tmp - tmp_2) > eps:
        count+=1
        answer += str(count) + '. ' + 'xi-1 = ' + str(tmp_1) + '; xi = ' + str(tmp_2) + '; \n'
        tmp = tmp_1
        tmp_1 = tmp_2
        tmp_2 = tmp - (f(tmp, x3, x2, x1, k) / f1(tmp, x3, x2, x1))

    answer += 'Ответ: ' + str(tmp) + ' | Количество итераций: ' + str(count)
    return answer


def func5(x3, x2, x1, k, a, b, eps):
    if (func5_check(a,b,k)):
        return 0
    MIN_RANGE = a
    MAX_RANGE = b
    EPS = eps
    answer = ''
    x = 5
    count = 0
    x = searchX(MIN_RANGE, MAX_RANGE,x, x3, x2, x1)
    lambd = getLambda(x, x3, x2, x1)
    x0 = x
    x = x - lambd * (pow(x, 3) + x2 * pow(x, 2) + x1 * x + k)
    fx = pow(x0, 3) + x2 * pow(x0, 2) + x1 * x0 + k
    answer += str(count) + '. ' + 'x0 = ' + str(x0) + '; fx = ' + str(fx) + '; \n'
    while abs(x - x0) >= EPS:
        x0 = x
        x = x - lambd * (pow(x, 3) + x2 * pow(x, 2) + x1 * x + k)
        fx = pow(x0, 3) + x2 * pow(x0, 2) + x1 * x0 + k
        count+=1
        answer += str(count) + '. ' + 'x0 = ' + str(x0) + '; fx = ' + str(fx) + '; \n'
    answer += 'Ответ: ' + str(x0)
    return answer



def func5_check(a, b, k):
    if (a-k>0):
        count_1 = 1/(3*pow(abs(a-k), -2/3))
    else:
        count_1 = 0
    if (b-k>0.0):
        count_2 = 1/(3*pow(abs(b-k), -2/3))
    else:
        count_2 = 0
    return (count_1 >= 1 and count_2 >= 1)

def f(x, x3, x2, x1, k):
    return x3*pow(x,3) + x2*pow(x,2) + x1*x + k


def f1(x, x3, x2, x1):
    return 3*x3*pow(x, 2) + 2*x2*x + x1

def f2(x, x3, x2):
    return 6*x3*x + 2*x2


def searchX(min_range, max_range, x, x3, x2, x1):
    a = 3 * x3 * pow(min_range, 2) - 2 * x2 * min_range - x1
    b = 3 * x3 * pow(max_range, 2) - 2 * x2 * max_range - x1
    c = 3 * x3 * pow(x, 2) - 2 * x2 * x - x1
    if a >= b and a >= c:
        return min_range
    else:
        if b >= a and b >= c:
            return max_range
        else:
            return x


def getLambda(x, x3, x2, x1):
    return 1 / (3 * x3 * pow(x, 2) - 2 * x2 * x - x1)


def printGraphFor5(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y1 = x
    y2 = f(x,x3,x2,x1,k)
    ax.plot(x, y1)
    ax.plot(x, y2)
    plt.show()


def printGraph(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y = f(x,x3,x2,x1,k)
    ax.plot(x, y)
    plt.show()


if __name__ == '__main__':
    answerGiven = True
    scannerline = True
    x3 = 1
    x2 = 4.81
    x1 = -17.37
    k = 5.38
    a = 0
    b = 3
    eps = 0.01

    while scannerline:
        print('Ввод из файла/из строки (1/0): ')
        mes = input()
        if mes == '1':
            try:
                pathh = open('lol', 'r')
                x3, x2, x1, k = map(float, pathh.readline().split(' '))
                a, b = map(float, pathh.readline().split(' '))
                eps = float(pathh.readline())

                answerGiven = True
                scannerline = False
            finally:
                pathh.close()
        else:
            print('Коэффициент перед x^3: ')
            x3 = float(input())
            print('Коэффициент перед x^2: ')
            x2 = float(input())
            print('Коэффициент перед x^1: ')
            x1 = float(input())
            print('Свободный член: ')
            k = float(input())
            print('Левая граница приближения: ')
            a = float(input())
            print('Правая граница приближения: ')
            b = float(input())
            print('Погрешность: ')
            eps = float(input())
            answerGiven = True
            scannerline = False

    print('Выберите метод: \n' +
          '1. Половинного деления \n' +
          '2. Метод Ньютона \n' +
          '3. Метод простой итерации \n' +
          'Ваш ответ: ')
    answer = ''


    while answerGiven:
        give = input()
        if give == '1':
            printGraph(a, b)
            answer = func1(x3, x2, x1, k, a, b, eps)
            answerGiven = False
        elif give == '2':
            printGraph(a, b)
            answer = func3(x3, x2, x1, k, b, eps)
            answerGiven = False
        elif give == '3':
            printGraphFor5(a, b)
            answer = func5(x3, x2, x1, k, a, b, eps)
            answerGiven = False
        else:
            print('Ошибка: не тот номер \n' +
                  'попробуйте еще раз')
            continue

    print('Вывести в файл/консоль(1/0)')
    viv = input()
    if viv == '1':
        try:
            with open('l.txt', 'w') as file:
                file.writelines(answer)
        except:
            print("Ошибка: решений нет")
        finally:
            file.close()
    else:
        if (answer!=0):
            print(answer)
        else:
            print("Ошибка: решений нет")
