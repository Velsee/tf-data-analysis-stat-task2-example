import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Расчет альфа
    alpha = 1 - p

    # Находим квантили стандартного нормального распределения
    z_left = norm.ppf(alpha / 2)
    z_right = norm.ppf(1 - alpha / 2)

    # Расчитываем выборочное среднее и дисперсию
    x_mean = np.mean(x)
    s_squared = np.var(x, ddof=1)

    # Расчет границ доверительного интервала
    lower_bound = (x_mean - 0.074) - (z_right * ((s_squared / len(x)) ** 0.5))
    upper_bound = (x_mean - 0.074) + (z_right * ((s_squared / len(x)) ** 0.5))

    # Возвращаем кортеж левой и правой границ доверительного интервала
    return lower_bound, upper_bound
