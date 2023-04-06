import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = x.shape[0]
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    
    q = norm.ppf(1 - (1 - p) / 2)  # квантиль нормального распределения
    left = mean - q * std / np.sqrt(n) - 0.074
    right = mean - q * std / np.sqrt(n)
    
    return (left, right)
