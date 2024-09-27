# code courtesy of Adam Dempsey
# modified for PHy1055 by Oisín Creaner
# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE


# import libraries
import matplotlib.pyplot as plt
import numpy as np


def grid_options(start, stop, stepsize=1, numpoints=11, option="linspace"):
    """
    This function demonstrates the difference between the arange and linspace methods of Numpy for creating
    ordered ranges of values. Some more ways of doing this are listed in G0_ranges.py   
    """
    if option == "arange":
        # arange creates a set of values between a start point and a stop point in steps of stepsize.
        # the stop point is usually excluded, but rounding errors may cause it to be included
        # this can be prevented using the argument endpoint=False
        x, y = np.meshgrid(np.arange(start, stop, stepsize), np.arange(start, stop, stepsize))
    elif option == "linspace":
        # linspace creates a set of numpoints values between a start point and a stop point
        # start point and stop point are both always included
        # note that the number of points is equal to the number of steps + 1
        # e.g. linspace(0, 5, 6) returns [0, 1, 2, 3, 4, 5]
        # while linspace (0, 5, 5) returns [0, 1.25, 2.5, 3.75, 5]
        x, y = np.meshgrid(np.linspace(start, stop, numpoints), np.linspace(start, stop, numpoints))
    else:
        raise NameError("Invalid option {} selected.".format(option))
    return x, y


def get_vector(x, y):
    """
    returns the vector field where vx = cos(x) and vy = sin(y)
    x and y may be floats or arrays
    vx and vy will be of the same type as x and y respectively
    x and y should be of the same length for most applications you'd use this for,
    but this function doesn't check
    """
    vx = np.cos(x)
    vy = np.sin(y)

    return vx, vy


def add_legend(x, y, vx, vy, x_pos=0.9, y_pos=0.9, key_size=2):
    """
    This function demonstrates how to add a key to your quiverplot. In addition to plotting the quiverplot
    It also puts the key at the x and y positions specified and with a size the user can specify
    """

    # plots the quiverplot. The return value of plt.quiver (an "Artist" datatype which contains the data
    # needed to draw the arrows) is returned to the variable q.
    q = plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')

    # This then is passed to plt.quiverkey so the key knows what data it represents
    plt.quiverkey(q, x_pos, y_pos, key_size, r'$2\frac{m}{s}$', labelpos='E', coordinates='figure')
    return q


def reduced_density(x, y, vx, vy, x_pos=0.9, y_pos=0.9, key_size=2, reduction=3):
    """
    This function demonstrates how to plot a quiver plot with a reduced density
    It is also overlaid with a scatterplot to show the exact pivot points
    """

    # plot the quiverplot with reduced density
    # Note the syntax of the indices is [start_point:stop_point:step_size]
    # By leaving start_point and stop_point blank, we indicate that we want to use the whole range of values
    # step_size in this case is in index steps in the array.
    # for example: arr[::3] would return [arr[0], arr[3], arr[6] ... arr[3N]]
    q = plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                   vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                   pivot='mid',  # position of the pivot of the arrow
                   label='$v_x$ = cos($x$), $v_y$ = sin($y$)')  # label using LaTex notation

    # creates the quiver key as above in the position specified
    plt.quiverkey(q, x_pos, y_pos, key_size, r'$2\frac{m}{s}$', labelpos='E', coordinates='figure')

    # plots a scatter plot with the same reduction factor
    # specifies the colour of the points and their size
    plt.scatter(x[::reduction, ::reduction], y[::reduction, ::reduction], color='r', s=10)



