# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE
from scipy import integrate


# PLACEHOLDER FUNCTION
def damped_pendulum(t, y, b, omega0):
    """
    The proper version of this function is defined in R4_function.
    What's here is just a placeholder.
    """
    pass


# PLACEHOLDER VARIABLES
# these don't do anything.  When you incorporate the code into your program
# these will be defined elsewhere in your code
t, y, b, omega0 = 0
t0, tf, y0 = 0

# below this line are the bits that you need to include
#######################################################

# define a lambda function in a proper program that takes these arguments
lfun = lambda t, y, : damped_pendulum(t, y, b, omega0)


# The part of the code running the solver then needs to read:
result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                             t_span=(t0, tf),  # Initial and final times
                             y0=y0,  # Initial state
                             method="RK45",  # Integration method
                             t_eval=t)  # Time points for result to be defined at
