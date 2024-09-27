# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# import libraries
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    plt.close()
    x, y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
    vx = np.cos(x)
    vy = np.sin(y)
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example of a quiver plot')
    plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')
    plt.legend()
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
