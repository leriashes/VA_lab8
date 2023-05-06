import numpy as np
import matplotlib.pyplot as plt
import math
import getch

def RungeKutta(funcy, funcz, yn, zn, h):
    y = yn
    z = zn

    print('\nРУНГЕ-КУТТА')

    k1 = h * eval(funcy)
    print('k1 = ', k1)

    m1 = h * eval(funcz)
    print('m1 = ', m1)


    y += k1/2
    z += m1/2

    k2 = h * eval(funcy)
    print('k2 = ', k2)

    m2 = h * eval(funcz)
    print('m2 = ', m2)


    y = yn + k2/2
    z = zn + m2/2

    k3 = h * eval(funcy)
    print('k3 = ', k3)

    m3 = h * eval(funcz)
    print('m3 = ', m3)


    y = yn + k3
    z = zn + m3

    k4 = h * eval(funcy)
    print('k4 = ', k4)

    m4 = h * eval(funcz)
    print('m4 = ', m4)

    result = [yn + (k1 + 2 * (k2 + k3) + k4) / 6, zn + (m1 + 2 * (m2 + m3) + m4) / 6]

    print('\n')
    print('y(n+1) = ', result[0])
    print('z(n+1) = ', result[1])

    print('\n')
    print('\n')

    return result


while True:
    while True:
        print('1 - с постоянным шагом\n2 - с автоматическим шагом\n\nВыберите режим работы программы: ', end='')
        variant = int(input())
        print('\n')

        if variant == 1 or variant == 2:
            break

    print('y = y(x)    z = z(x)\n')

    print('Введите уравнения системы: \ny\' = ', end='')
    funcy = input()

    print('z\' = ', end='')
    funcz = input()
    print('\n')

    print('Введите левую границу отрезка: x0 = a = ', end='')
    a = float(input())

    while True:
        print('Введите правую границу отрезка: x0 + X = b = ', end='')
        b = float(input())
        print('\n')

        if b > a:
            break

    print('Отрезок: [', a, ', ', b, ']\n', sep='')

    print('Введите начальные условия:\ny(x0) = y(', a, ') = ', sep='', end='')
    y0 = float(input())

    print('z(x0) = z(', a, ') = ', sep='', end='')
    z0 = float(input())
    print('\n')

    if variant == 1:
        while True:
            print('Введите шаг: h = ', end='')
            h = float(input())
            print('\n')

            if h <= b - a:
                break

    print('Введите аналитическое решение системы: \ny = ', end='')
    fy = input()

    print('z = ', end='')
    fz = input()
    print('\n')

    result = [y0, z0]

    xs = [a]
    ys = [y0]
    zs = [z0]

    ya = [y0]
    za = [z0]

    x = a
    while (x < b):
        print('x = ', x)
        result = RungeKutta(funcy, funcz, result[0], result[1], h)
        ys.append(result[0])
        zs.append(result[1])
        x += h
        xs.append(x)

        ya.append(eval(fy))
        za.append(eval(fz))

    plt.plot(xs, ya, 'g')
    plt.plot(xs, za, 'b')
    
    plt.plot(xs, ys, 'r')
    plt.plot(xs, zs, 'purple')
    plt.grid(True)

    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$y$', fontsize=14)

    plt.show()


    while True:
        print('Введите допустимую относительную погрешность: eps = ', end='')
        eps = float(input())
        print('\n')

        if eps > 0:
            break

    
    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='\n')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break

