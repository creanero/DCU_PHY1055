# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE
import matplotlib.pyplot as plt
from scipy import integrate


def driven_pendulum():
    """
    PLACEHOLDER: define this function yourself based on the previous damped_pendulum function
    """
    pass


def loop_through(omega, b, tf, y0):
    """
        THIS ISN'T REALLY A USABLE FUNCTION. IT'S INTENDED TO BE MERGED INTO YOUR REAL CODE

        This code plots the response for three different driving frequencies and displays
        the results on the same graph. It's important to note that the command plot(t,x)
        is placed within the loop.
    """

    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for omegad in (omega, 0.9 * omega, 0.5 * omega):
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y,: driven_pendulum(t, y, b, omega, omegad)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)
        # Store result of this run in variables t, x, v
        t = result.t
        x, v = result.y
        # Plot the result x(t) for this run, lable it with omegad as well
        plt.plot(t, x, label='$x(t): \omega_d =${}'.format(omegad))
    # End of loop, continue with next omegad
    # Out of the loop
    # Save and show plot
    plt.legend()  # Make the plot labels visible
    plt.savefig('Oscillator-driven-multi.pdf', bbox_inches ='tight')
    plt.show()

