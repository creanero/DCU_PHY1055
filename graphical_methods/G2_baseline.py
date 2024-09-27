# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.close()

    # Create Grid
    coords = np.linspace(-2, 2, 101)
    x, y = np.meshgrid(coords, coords)

    # Create Function and gradient
    z = np.exp(-(x**2 + y**2))
    dx, dy = np.gradient(z)  # Calculate the gradient

    # Create Figure
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D exponential function: $f(x,y)=e^{-(x^2+y^2)}$')

    # Plot scalar function as color plot (contour map)
    plt.contourf(x, y, z, 20)  # plot a contour map using N=20 levels
    plt.set_cmap('coolwarm')  # change color of map

    # Plot Gradient as quiver plot
    skip = 5  # Number of points to skip

    # create coarse grid
    x_skipped, y_skipped = x[::skip, ::skip], y[::skip, ::skip]  # note the indexing [start:end:skip]
    dx_skipped, dy_skipped = dx.T[::skip, ::skip], dy.T[::skip, ::skip]  # note the .T transpose method

    # plot the gradient using the coarse grid and a quiverplot.
    plt.quiver(x_skipped, y_skipped, dx_skipped, dy_skipped, scale=0.8)
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
