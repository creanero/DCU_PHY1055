# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# define the nonlinear defivative function
def Nonlinear1(t,y):
    dydt = -y**3 + np.sin(t)
    return(dydt)

# define the initial variables
y0 = np.array([0]) # initial state at t = 0
t0 = 0 # initial time
tf = 20 # final time
n = 101 # Number of points at which output will be evaluated (note 101 points are needed for 100 spaces)
# Note: this does not mean the integrator will take only n steps SciPy
# will control this to control the error in the solution

# create a numpy array of n times linearly spaced between t0 and tf
t = np.linspace(t0, tf, n)

# Call the RK integrator and return the solution in the array "result"
# Note that that because the brackets aren't closed, the integrate.solve_ivp operation
# behaves as though it was on just one line.
result = integrate.solve_ivp(fun = Nonlinear1, # The function defining the derivative
                             t_span = (t0, tf), # Initial and final times
                             y0 = y0 , # Initial state
                             method = "RK45", # Integration method
                             t_eval = t ) # Time points for result to be reported

# Read the solution and time from the array returned by Scipy
y = result.y[0]
t = result.t

# plot the solution
plt.plot(t,y,’b.’)
plt.show()