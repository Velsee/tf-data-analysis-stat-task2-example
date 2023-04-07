import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    b_mean = 4*x.mean() - 0.074
    z = norm.ppf(1-p/2)
    sd = x.std(ddof=1)
    b_left = b_mean - z * sd / np.sqrt(len(x)) 
    b_right = b_mean + z * sd / np.sqrt(len(x))
    return (b_left, b_right)
