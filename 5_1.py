# -*- coding: utf-8 -*-
"""5.1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BWmMh5Br53qIZ_9emn0evJFIMv6o_Y3Q
"""

import numpy as np
import matplotlib.pyplot as plt

# Создаем двумерный массив с данными о температуре
# Размер региона 20x20, температурный диапазон [-20, 30]
temperature_data = np.random.uniform(-20, 30, (20, 20))

# Создаем тепловую карту
plt.figure(figsize=(10, 8))
plt.imshow(temperature_data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Температура (°C)')
plt.title('Тепловая карта температуры')
plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.show()