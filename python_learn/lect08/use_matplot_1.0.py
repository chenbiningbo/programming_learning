"""
    作者：陈笔
    版本：1.0
    功能：matplot使用
    日期：10/08/2019
"""
from pylab import *

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()