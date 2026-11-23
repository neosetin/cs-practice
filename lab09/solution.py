import numpy as np


def make_hours():
    hrs = np.arange(0, 22, 3)
    return hrs.tolist()


def vector_report(values):
    vec = np.asarray(values, dtype=float)
    report = {
        "third": float(vec.item(2)),
        "last": float(vec.item(-1)),
        "middle": vec[2:6].tolist(),
        "every_second": vec[::2].tolist(),
        "reversed": vec[::-1].tolist(),
    }
    return report


def change_vector(values):
    res_vec = np.asarray(values, dtype=float).copy()
    res_vec[2:5] = 99
    res_vec[::2] = -1
    return res_vec.tolist()


def cap_above(values, limit):
    temp_arr = np.asarray(values, dtype=float).copy()
    temp_arr[temp_arr > limit] = limit
    return temp_arr.tolist()


def celsius_to_fahrenheit(values):
    c_arr = np.asarray(values, dtype=float)
    f_arr = c_arr * 9 / 5 + 32
    return f_arr.tolist()

