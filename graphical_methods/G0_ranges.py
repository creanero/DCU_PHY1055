# Created for PHY1055 by Oisín Creaner
import numpy as np
import matplotlib.pyplot as plt


def linspace_demo():
    """
    np.linspace() takes three arguments:
    a start point (x0), a stop point (xf) and a number of points (N).
    It returns a Numpy array, with N evenly spaced values,
    starting with x0 and ending with xf.
    For example, np.linspace(0, 5, 6) returns [0. 1. 2. 3. 4. 5.],
    while np.linspace (0, 5, 5) returns [0. 1.25 2.5 3.75 5.0].
    """

    # sets up control variables
    start = 0.5
    stop = 4.5
    numpoints = 5

    # creates a linspace with the values specified
    linspace_result = np.linspace(start, stop, numpoints)

    # prints the return value. Note that because the brackets haven't been closed,
    # we can continue the command over multiple lines.
    print("linspace(start={}, stop={}, numpoints={}) \nreturns {}\n"
          .format(start, stop, numpoints, linspace_result))

    return linspace_result


def arange_demo():
    """
    Another useful tool is np.arange().
    It also takes three arguments:
    a start point (x0), a stop point (xf) but now a step-size (S) instead of a number of points.
    It also returns a Numpy array, again starting with x0,
    this time with values separated by S and ending at or before xf.
    For example, np.arange(0, 5, 1) returns [0 1 2 3 4].
    However, the endpoint may be included due to floating point rounding errors, so be aware of that
    For example, np.arange(1, 1.3, 0.1) returns [1. 1.1 1.2 1.3]
    if you need to be sure the endpoint isn't included, use the argument endpoint=False
    For example, np.arange(1, 1.3, 0.1, endpoint=False) returns [1.  1.1 1.2]
    """

    # sets up control variables
    start = 0
    stop = 5
    stepsize = 1

    # creates an arange with the specified parameters
    arange_result = np.arange(start, stop, stepsize)

    # prints the return value. Note that because the brackets haven't been closed,
    # we can continue the command over multiple lines.
    print("arange(start={}, stop={}, stepsize={}) \nreturns {}\n"
          .format(start, stop, stepsize, arange_result))

    return arange_result


def meshgrid_demo(x_points, y_points, label):
    """
    Meshgrid takes two or more arrays as arguments (we'll use two for the moment)
    Each argument corresponds to the points along one of the dimensions we want to create a grid of.
    In our case, that means we supply the x and y co-ordinates using a linspace or arange.
    It returns two, 2-D arrays, each of which iterates through the elements of the input arrays
    but along different axes.

    For example,
    x_points=[0, 1, 2]
    y_points=[3, 4, 5, 6]
    x_mesh, y_mesh = np.meshgrid(x_points, y_points)

    would return
    x_mesh = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    y_mesh = [[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]

    This corresponds to the grid points
    (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5), (0, 6), (1, 6), (2, 6)
    That is a rectangular grid of three points in the x-direction and four in the y-direction from
    (0, 3) to (2, 6)
    """
    # creates a mesh using the x- and y- points provided
    x_mesh, y_mesh = np.meshgrid(x_points, y_points)
    # prints the array to the screen
    print("meshgrid(x={0}, y=linspace_{0})"
          "\nreturns "
          "\nx={1}"
          "\ny={2}"
          "\n See plot!\n"
          .format(label, x_mesh, y_mesh))
    # plots a graph
    plt.scatter(x_mesh, y_mesh, label=label)


def mesh_plot(linspace_result, arange_result):
    # sets up the plots
    plt.figure()
    plt.title("Comparison of using linspace and arange with meshgrid.")
    plt.xlabel("x")
    plt.ylabel("y")

    # creates a mesh using the linspace settings
    meshgrid_demo(linspace_result, linspace_result, "linspace_result")

    # creates a mesh using the arange settings
    meshgrid_demo(arange_result, arange_result, label="arange")

    # you can even make a mesh with a mix of both. The dimensions don't even have to be the same length!
    x_points = arange_result
    try:
        y_points = linspace_result[1:-1]  # note the indexing: from index one from the start to one from the end
    except IndexError:  # if linspace result is defined such that the indexing doesn't work
        y_points = linspace_result
    meshgrid_demo(x_points, y_points, label="mix")

    # includes a legend on the plot
    plt.legend()

    # displays the plots on the screen
    plt.show()


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    # runs our linspace demonstration
    linspace_result = linspace_demo()

    # runs our arange demonstration
    arange_result = arange_demo()

    # runs our meshgrid demo
    mesh_plot(linspace_result, arange_result)


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()

