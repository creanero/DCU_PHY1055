# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

import numpy as np
import matplotlib.pyplot as plt


def E(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


def main():
    # Grid of x, y points
    d = 128
    x = np.linspace(-2, 2, d)
    y = np.linspace(-2, 2, d)
    X, Y = np.meshgrid(x, y)

    # Create a multipole with nq charges of alternating sign,
    # equally spaced on the unit circle.
    nq = 8  # Define the number of charges here

    charges = []
    for i in range(nq):
        q = i % 2 * 2 - 1
        charges.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

    # Electric field vector, E=(Ex, Ey), as separate components
    Ex, Ey = np.zeros((d, d)), np.zeros((d, d))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey

    plt.figure(figsize=(5, 5))
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.streamplot(X, Y, Ex, Ey, density=2, color='gray', linewidth=0.5)

    # Add filled circles for the charges themselves
    charge_colors = {True: '#cc0000', False: '#0000cc'}
    for q, pos in charges:
        plt.scatter(pos[0], pos[1], s=100, color=charge_colors[q > 0])

    plt.show()

# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
