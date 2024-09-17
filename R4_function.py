import numpy as np


def damped_pendulum(t, y, b=0.1, omega0=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt
