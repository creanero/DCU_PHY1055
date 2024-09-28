# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, y = np.meshgrid(coords, coords)
    dx = -1 - x**2 + y
    dy = 1 + x - y**2
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Vector field: $f(x,y)=(-1-x^2+y, 1+x-y^2)$')
    plt.quiver(x, y, dx, dy)  # plot field as quiver
    plt.streamplot(x, y, dx, dy)  # plot streamlines of field.
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
