""""
Напишите функцию, которая находит две точки: где наклон графика
функции самый крутой (в любую сторону), где наклон самый пологий,
и отображает на графике функции эти точки зелёным и красным кругом соответственно.
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = x * x * np.sin(x / 300) + 300 * x
    return y


def plot_func_dep(f, a, b):
    x = np.arange(a, b)

    # Значения нашей функции
    y = [f(i) for i in x]

    # Производная
    len_x = x.shape[0]
    df = np.array([f(x[i + 1]) - f(x[i]) for i in range(len_x - 1)])

    # Максимальное значение производной - там функция растет быстрее всего
    df_max = np.max(df)

    # Массивы для записи точек
    depr_max = []
    depr_zero = []

    # Проходимся циклом по значениям производной и записываем
    # Максимальное значение - наклон графика функции самый крутой
    for i in range(len(y) - 1):
        if df[i] == df_max:
            depr_max.append(i)

        # Пересечение с 0 и плато
        if df[i - 1] > 0 and df[i + 1] < 0:
            depr_zero.append(i)

    # Строим графики
    # Строим график функции
    plt.plot(x, y)
    # График производной
    plt.plot(x[:-1], df * 100)
    # Ось ох
    plt.plot(x, np.array([0 for i in range(a, b)]))
    # Точки, где наклон графика функции самый крутой
    plt.plot([x[i] for i in depr_max], [y[i] for i in depr_max], 'go')

    # Точки, где плато или самый пологий угл
    plt.plot([x[i] for i in depr_zero], [y[i] for i in depr_zero], 'ro')
    plt.show()


plot_func_dep(f, -10000, 10000)