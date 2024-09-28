# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE
import matplotlib.pyplot as plt


def multiple_plot_rf(r_mesh, f_mesh, dr, df, r, f, t):
    """
    You could import this function and use it in the Lotka-Volterra model.
    I would suggest you find a more elegant solution than that.

    When exploring options for parameters of ODEs it is useful to plot more than one specific quantity. For example in
    the LVM model it is helpful to look at vectors, time series, phase plots simultaneously.
    The following code illustrates how mathplotlib is used to combine plots into one figure.

    :param r_mesh: a meshgrid of possible values for rabbit population
    :param f_mesh: a meshgrid of possible values for fox population
    :param dr: the expected changes in rabbit population at a given point in the mesh
    :param df: the expected changes in fox population at a given point in the mesh
    :param r: array containing a set of rabbit populations over time given particular initial conditions
    :param f: array containing a set of fox populations over time given particular initial conditions
    :param t: array containing a set of points in time
    :return: None
    """
    # Set up 3 panel figure
    plt.close()
    plt.figure(figsize=(14, 5))

    # first column figure: Vectorfield
    plt.subplot(1, 3, 1)
    plt.quiver(r_mesh, f_mesh, dr, df, pivot='mid')
    plt.xlabel(r"$rabbits$")
    plt.ylabel(r"$foxes$")

    # second column figure: Time series
    plt.subplot(1, 3, 2)
    plt.plot(t, r, 'b-', label='rabbits')
    plt.plot(t, f, 'g-.', label='foxes')
    plt.ylabel('number')
    plt.xlabel('time')
    plt.legend(loc='upper right')

    # third column figure: Fox-Rabbit Phase
    plt.subplot(1,3,3)
    plt.plot(r, f, 'k', color='brown')
    plt.ylabel(r"$foxes$")
    plt.xlabel(r"$rabbits$")

    # this will save the figure as a PDF in the directory you're running it from: is that what you want?
    plt.savefig('rab-fox-time-quiver.pdf', bbox_inches='tight')