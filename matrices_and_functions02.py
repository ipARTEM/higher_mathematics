"""
Напишите функцию, которая находит все экстремумы двумерной функции z = sin(x) * sin(y) в диапазоне [x = -3.14, x = 3.14], [y = -3.14, y = 3.14], а также:

a) Возвращает листы с координатами двумерных точек - 4 листа - локальный и глобальный минимум и максимум.

b) Выводит график такой функции.
"""

# Подключение библиотек для отображения 3d поверхностей
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

import pylab, math
from mpl_toolkits.mplot3d import Axes3D


# Функция x * x * sin (y)
def x2_sin(x, y):
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = np.sin(xgrid) * np.sin(ygrid)
    return xgrid, ygrid, zgrid


# Поиск экстремумов
def find_extremums(f, x, y):
    # Вычислим функцию
    xgrid, ygrid, zgrid = f(x, y)
    print(xgrid)
    print('***')
    print(zgrid)

    # Пустые листы для экстремумов
    local_mins = []  # Локальные минимумы
    local_maxs = []  # Локальные максимумы
    global_min = []  # Глобальный минимум
    global_max = []  # Глобальный максимум

    # Минимальное и максимальное значение y
    min_z = round(np.amin(zgrid), 5)  # Округляем до 5го знака
    max_z = round(np.amax(zgrid), 5)  # Округляем до 5го знака
    zi, zj = zgrid.shape

    # Проходим во всем точкам
    for i in range(zi):
        for j in range(zj):
            # Если точка равна минимуму y
            # То это глобальный минимум
            if (round(zgrid[i, j], 5) == min_z):
                global_min.append([xgrid[0, j], ygrid[i, 0], zgrid[i, j]])  # Заносим координату в список минимумов

            # Если точка равна максимуму y
            # То это глобальный максимум
            if (round(zgrid[i, j], 5) == max_z):
                global_max.append([xgrid[0, j], ygrid[i, 0], zgrid[i, j]])  # Заносим координату в список максимумов

            # Если это не первая и не последняя точка
            # (в них не можем считать локальные минимум и максимум)
            if (i > 0 and i < zi - 1 and j > 0 and j < zj - 1):
                # Если точка меньше, чем соседние
                if (zgrid[i - 1, j - 1] > zgrid[i, j]
                        and zgrid[i + 1, j + 1] > zgrid[i, j]
                        and zgrid[i + 1, j - 1] > zgrid[i, j]
                        and zgrid[i - 1, j + 1] > zgrid[i, j]
                        and zgrid[i - 1, j] > zgrid[i, j]
                        and zgrid[i + 1, j] > zgrid[i, j]
                        and zgrid[i, j - 1] > zgrid[i, j]
                        and zgrid[i, j + 1] > zgrid[i, j]):
                    local_mins.append(
                        [xgrid[0, j], ygrid[i, 0], zgrid[i, j]])  # То это локальный минимум (по всем направлениям)

                # Если точка больше, чем соседние
                if (zgrid[i - 1, j - 1] < zgrid[i, j]
                        and zgrid[i + 1, j + 1] < zgrid[i, j]
                        and zgrid[i + 1, j - 1] < zgrid[i, j]
                        and zgrid[i - 1, j + 1] < zgrid[i, j]
                        and zgrid[i - 1, j] < zgrid[i, j]
                        and zgrid[i + 1, j] < zgrid[i, j]
                        and zgrid[i, j - 1] < zgrid[i, j]
                        and zgrid[i, j + 1] < zgrid[i, j]):
                    local_maxs.append(
                        [xgrid[0, j], ygrid[i, 0], zgrid[i, j]])  # То это локальный максимум (по всем направлениям)

    return local_mins, local_maxs, global_min, global_max


# Функция для вывода точек
def plot_points(points, axes, marker='ro'):
    if len(points) > 0:  # Проверка на пустой список
        coords = np.transpose(np.array(points))  # Транспонируем для получения массива из трех координат
        axes.plot(coords[0], coords[1], coords[2], marker, markersize=10, alpha=1, zorder=99)
        return coords
    else:
        return np.array([])


# Выводим поверхность z = x * x * sin(y)
fig = pylab.figure(figsize=(10, 10))
axes = Axes3D(fig)
y = np.arange(-math.pi, math.pi, 0.1)
x = np.arange(-10, 10, 0.1)
xgrid, ygrid, zgrid = x2_sin(x, y)
axes.plot_surface(xgrid, ygrid, zgrid)

# Получаем экстремумы
local_mins, local_maxs, global_min, global_max = find_extremums(x2_sin, x, y)

# Выводим точки
plot_points(local_mins, axes, 'go')
plot_points(local_maxs, axes, 'ro')
plot_points(global_min, axes, 'gs')
plot_points(global_max, axes, 'rs')
pylab.show()

# Выводим списки всех точек
print("Локальные минимумы", local_mins, sep='\n')
print("Локальные максимумы", local_maxs, sep='\n')
print("Глобальный минимум", global_min, sep='\n')
print("Глобальный максимум", global_max, sep='\n')
