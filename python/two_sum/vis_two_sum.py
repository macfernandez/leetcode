import time
import pandas as pd
from typing import *
import seaborn as sns
import matplotlib.pyplot as plt

from python.two_sum.two_sum import Solution

cases = [
    (
        [3,3],
        6
    ),
    (
        [3,2,4],
        6
    ),
    (
        [2,7,11,15],
        9
    ),
    (
        [
            -106, 49, 52, 108, -41,
            34, 64, -75, 28, 6,
            89, -99, 45, 9, 39,
            29, -7, -39, -85, -87,
            66, -23, 1, 31, -91,
            -35, 76, 92, 71, 91,
            -73, 22, 48, -26, -1,
            96, -37, -24, 67, -102,
            18, -33, -34, -96, 36,
            -30, -5, -61, -38, -103,
            -108, -100, -95, -47, -19,
            -76, 43, 11, -88, 5,
            -67, 41, -55, -42, 84,
            -29, -82, 85, -59, 3,
            4, 33, -2, 70, 58
        ],
        108
    ),
    (
        [
            -12, -21, -79, 18, -2,
            10, -13, -66, 54, 2,
            17, 1, -48, -6, -97,
            75, -61, -86, 74, -109,
            -39, 0, -24, -54, 23
        ],
        42
    ),
    (
        [
            -14, -82, -28, 6, 13,
            -4, 29, -74, 66, 19,
            8, 48, 20, -36, 31,
            -9, 79, 40, 5, -57,
            76, -42, -61, -62, 44,
            78, -41, 33, 69, -38,
            101, 4, -76, -108, 88,
            105, -46, -68, -22, -73,
            -19, 85, -29, 90, -80,
            -50, -1, -13, 11, -51
        ],
        -94
    ),
    (
        [
            82, 23, 55, -15, 11,
            -16, 21, -18, 72, -6,
            0, 75, 38, 43, 104,
            -79, -98, 61, -86, -48,
            -57, -61, -60, -82, -109,
            44, -72, 74, -1, -43,
            -91, 39, -46, -69, -81,
            84, 27, -11, -35, 36,
            -50,34, 17, 31, 52,
            80, -65, 54, 65, 92,
            -7, -8, 88, -45, -78,
            -51, -68, 53, 59, -88,
            -97, -66, -25, -56, -20,
            94, -52, -13, 1, 5,
            7, 22, -31, 37, 86,
            -27, -76, -75, 42, -84,
            9, -106, -102, -26, -9,
            -83, 71, -23, 30, 4,
            -100, -96, -10, 104, 49,
            -5, -3, 85, 102, -59,
            -55, -54, 24, -19
        ],
        100
    )
]

def apply_func(func:callable, **kwargs):
    st = time.time()
    func(**kwargs)
    et = time.time()
    elapsed_time = et - st
    return elapsed_time

df = pd.DataFrame(cases, columns=['nums','target'])
df['nums_len'] = df.nums.apply(len)
df['two_sum'] = df.apply(
    lambda x: apply_func(
        Solution().two_sum,
        nums=x.nums,
        target=x.target),
    axis=1
)
df['two_sum_faster'] = df.apply(
    lambda x: apply_func(
        Solution().two_sum_faster,
        nums=x.nums,
        target=x.target
    ),
    axis=1
)
df_melt = df.melt(
    id_vars='nums_len',
    value_vars=['two_sum','two_sum_faster'],var_name='function',
    value_name='time_execution'
)

fig, ax = plt.subplots()
sns.lineplot(
    data=df_melt,
    x='nums_len',
    y='time_execution',
    hue='function'
)
plt.show()
