import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    b = 0.074 + (1 - 0.074) * p
    b_min = 0.074 + (1 - 0.074) * np.min(x)
    b_max = 0.074 + (1 - 0.074) * np.max(x)
    return (b_min, b_max)
