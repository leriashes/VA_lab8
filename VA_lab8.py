import numpy as np
import matplotlib.pyplot as plt
import math
import getch

def RungeKutta(funcy, funcz, yn, zn, h):
    y = yn
    z = zn

    k1 = h * eval(funcy)
    #print('k1 =', k1, end=' ')

    m1 = h * eval(funcz)
    #print('m1 =', m1)


    y += k1/2
    z += m1/2

    k2 = h * eval(funcy)
    #print('k2 =', k2, end=' ')

    m2 = h * eval(funcz)
    #print('m2 =', m2)


    y = yn + k2/2
    z = zn + m2/2

    k3 = h * eval(funcy)
    #print('k3 =', k3, end=' ')

    m3 = h * eval(funcz)
    #print('m3 =', m3)


    y = yn + k3
    z = zn + m3

    k4 = h * eval(funcy)
    #print('k4 =', k4, end=' ')

    m4 = h * eval(funcz)
    #print('m4 =', m4)

    result = [yn + (k1 + 2 * (k2 + k3) + k4) / 6, zn + (m1 + 2 * (m2 + m3) + m4) / 6]

    return result


#метод Рунге для поиска автоматического шага
def Runge(funcy, funcz, yn, zn, h, eps):
    ready = False

    while not ready:
        res1 = RungeKutta(funcy, funcz, yn, zn, 2 * h)

        res2 = RungeKutta(funcy, funcz, yn, zn, h)
        res2 = RungeKutta(funcy, funcz, res2[0], res2[1], h)

        if abs(res1[0] - res2[0]) / 15 <= eps and abs(res1[1] - res2[1]) / 15 <= eps:
            ready = True
        else:
            h /= 2

    return h


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
    else:
        while True:
            print('Введите eps = ', end='')
            eps = float(input())
            print('\n')

            if eps > 0:
                break

        h = Runge(funcy, funcz, y0, z0, 1, eps)
        print('Автоматический шаг h = ', h)


    print('Введите аналитическое решение системы: \ny = ', end='')
    fy = input()

    print('z = ', end='')
    fz = input()
    print('\n')

    result = [y0, z0]

    xs = []
    ys = [y0]
    zs = [z0]

    ya = []
    za = []

    x = a
    i = 0
    normay = 0
    normaz = 0

    with open('result.csv', 'w') as file:
        file.write('i;x;y(x);z(x)\n')
        while (x < b):
            xs.append(x)
            ya.append(eval(fy))
            za.append(eval(fz))

            file.write(str(i) + ';\'' + str(x) + ';\'' + str(ys[i]) + ';\'' + str(zs[i]) + '\n')
            result = RungeKutta(funcy, funcz, result[0], result[1], h)
            ys.append(result[0])
            zs.append(result[1])
            x += h

            if (x > 5.5):
                x = x

            if variant == 1:
                delta = abs(ya[i] - ys[i])
                if delta > normay:
                    normay = delta

                delta = abs(za[i] - zs[i])
                if delta > normaz:
                    normaz = delta

            i += 1

        x = b
        xs.append(x)

        file.write(str(i) + ';\'' + str(x) + ';\'' + str(ys[i]) + ';\'' + str(zs[i]) + '\n')

        ya.append(eval(fy))
        za.append(eval(fz))

    if variant == 1:
        delta = abs(ya[i] - ys[i])
        if delta > normay:
            normay = delta

        delta = abs(za[i] - zs[i])
        if delta > normaz:
            normaz = delta
                

        print('Норма уклонения от точного решения для y:', normay)
        print('Норма уклонения от точного решения для z:', normaz)

    plt.plot(xs, ya, 'g')
    plt.plot(xs, za, 'b')
    
    plt.plot(xs, ys, 'r', label=r'y(x)')
    plt.plot(xs, zs, 'purple', label=r'z(x)')
    plt.grid(True)

    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$y$', fontsize=14)
    plt.legend(loc='best', fontsize=12)
    plt.show()

    while True:
        print('Запустить исследование зависимости от шага итегрирования для нормы отклонения?\ny - да \nn - нет')
        cont = getch.getch()
   
        if cont == b'y':
            nz = []
            ny = []
            hs = []

            h = 1
            for i in range(16):
                hs.append(h)

                result = [y0, z0]
                xs = []
                ys = [y0]
                zs = [z0]

                ya = []
                za = []

                x = a
                j = 0
                normay = 0
                normaz = 0

                while (x < b):
                    xs.append(x)
                    ya.append(eval(fy))
                    za.append(eval(fz))
                    
                    result = RungeKutta(funcy, funcz, result[0], result[1], h)
                    ys.append(result[0])
                    zs.append(result[1])
                    x += h
                    
                    delta = abs(ya[j] - ys[j])
                    if delta > normay:
                        normay = delta

                    delta = abs(za[j] - zs[j])
                    if delta > normaz:
                        normaz = delta

                    j += 1

                x = b
                xs.append(x)
               
                ya.append(eval(fy))
                za.append(eval(fz))

                delta = abs(ya[j] - ys[j])
                if delta > normay:
                    normay = delta

                delta = abs(za[j] - zs[j])
                if delta > normaz:
                    normaz = delta

                ny.append(normay)
                nz.append(normaz)
                h /= 2

            plt.plot(hs, ny, 'g')
            plt.plot(hs, nz, 'b')
    
            plt.grid(True)

            plt.xlabel(r'$Шаг$', fontsize=14)
            plt.ylabel(r'$Норма отклонения$', fontsize=14)
            plt.legend(loc='best', fontsize=12)
            plt.show()
            break
        elif cont == b'n':
            break


    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='\n')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break

