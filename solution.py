import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)  # исправленное стандартное отклонение
    
    # находим критическое значение стандартного нормального распределения
    z = norm.ppf(1 - alpha / 2)
    
    # находим границы доверительного интервала
    left = mean - z * std / np.sqrt(n)
    right = mean + z * std / np.sqrt(n)

    return (left, right)
