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
    X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
    Vx = np.cos(X)
    Vy = np.sin(Y)
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box') #Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example of a quiver plot')
    plt.quiver(X, Y, Vx, Vy, pivot='mid', label='$V_x$ = cos($x$), $V_y$ = sin($y$)')
    plt.legend()
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
