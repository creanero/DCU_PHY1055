# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate
from pathlib import Path


def simple_pendulum(t, y):
    """
    Define the two derivatives
    note that dydt is now an array that holds both of the derivatives
    :param t: an array of times (floats) - not used in this template
    :param y: a tuple containing the values x and v
    :return: the derivative of x and v
    """
    x, v = y  # extracts the x and v values from the tuple
    dydt = np.array([v, -x])  # generates an array with the rates of change: dxdt = v, dvdt = -x
    return dydt  # returns the array


def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """

    # define the initial parameters
    x0 = 0  # initial position
    v0 = 1  # initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time

    # define the final time and the number of time steps
    tf = 10*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution

    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    # Calls the method integrate.solve_ivp()
    result = integrate.solve_ivp(fun=simple_pendulum,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",  # Integration method
                                 t_eval=t)  # Time points for result to be defined at

    # Read the solution and time from the result array returned by Scipy
    x, v = result.y
    t = result.t

    # plot position ad velocity as a function of time.
    plt.plot(t, x, label=r"$x(t)$")
    plt.plot(t, v, label=r"$v(t)$")
    plt.legend(loc=1)

    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='Harmonic-init', extension='png')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()
