import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Находим среднее значение выборки
    x_mean = x.mean()
    
    # Находим выборочную дисперсию
    x_var = np.var(x, ddof=1)
    # Находим квантили нормального распределения
    q_low = norm.ppf((1-p)/2)
    q_high = norm.ppf((1+p)/2)
    
    # Находим левую и правую границы доверительного интервала
    lower_bound = x_mean + q_low * np.sqrt(x_var/len(x)) - 0.074
    upper_bound = x_mean + q_high * np.sqrt(x_var/len(x)) - 0.074
    
    # Возвращаем кортеж с левой и правой границами доверительного интервала
    return (lower_bound, upper_bound)
