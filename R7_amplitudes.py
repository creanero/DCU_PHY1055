# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def driven_pendulum(t, y, b, omega_0, omega_d, y0):
    """
    PLACEHOLDER: define this function yourself based on the previous damped_pendulum function
    """
    pass


def placeholder_amplitudes(tf, n, omega_0, b, y0):
    amplitudes = []  # Create empty list to store amplitudes
    t = np.linspace(0.8*tf, tf, n)  # Change time array to include only later points

    driving_freq = np.linspace(0, 2*omega_0, 100)  # Create range of omega_d 20%-200% of omega_0

    for omega_d in driving_freq:  # Loop through driving frequencies
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y, : driven_pendulum(t, y, b, omega_0, omega_d)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)

        # Store result of this run in variables t, x, v
        t = result.t
        v, x = result.y

        amplitudes.append((max(x)-min(x))/2)  # Find peak to peak amplitude
        # End of loop, continue with next omegad
    # Out of the loop
    plt.plot(driving_freq, amplitudes) # Plot the amplitudes
