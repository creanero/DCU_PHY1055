# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt


def phase_space():
    # when you merge this into R3_template, you will use the values of v and x in that program
    v = []
    x = []

    # create a plot
    plt.figure()

    # plots v against x in black ('k')
    plt.plot(v, x, 'k')

    # sets the axes to equal sizes
    plt.axis('equal')

    # labels the axes
    plt.xlabel(r"$x$")
    plt.ylabel(r"$v$")
