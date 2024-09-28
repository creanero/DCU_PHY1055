# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# THIS ISN'T WORKING CODE. IT ONLY WORKS IF YOU CORRECTLY INCORPORATE IT INTO YOUR CODE
import matplotlib.pyplot as plt


def demo_multiplot(t, x, v):
    """
    THIS ISN'T REALLY A USABLE FUNCTION. IT'S INTENDED TO BE MERGED INTO YOUR REAL CODE

    If you have a given solution and want to create multiple plots from the same result,
    you can call the plot functions multiple times, saving individual plots.
    """
    plt.close()

    # plot the first figure
    plt.figure()
    plt.plot(t, x, label='$x(t)$')
    plt.plot(t, v, label='$v(t)$')

    # this will save the figure as a PDF in the directory you're running it from: is that what you want?
    plt.savefig('Solution.pdf', bbox_inches='tight')

    # plot the second figure
    plt.figure()
    plt.plot(v,x,'k')
    plt.axis('equal')

    # this will save the figure as a PDF in the directory you're running it from: is that what you want?
    plt.savefig('Phase.pdf', bbox_inches='tight')


def demo_combined_plot(t, x, v):
    """
    THIS ISN'T REALLY A USABLE FUNCTION. IT'S INTENDED TO BE MERGED INTO YOUR REAL CODE

    A more elegant approach is to use the inbuilt subplot function
    to create multiple graphs within one figure and file.
    """
    plt.close()

    # create the full figure
    plt.figure(figsize=(9, 4))  # Figure size in inch
    plt.subplots_adjust(wspace=0.3)  # Change horizontal separation if needed

    # Define first panel
    plt.subplot(1, 2, 1)  # (nrows, ncols, plot_number)
    plt.plot(t, x, label='$x(t)$')
    plt.plot(t, v, label='$v(t)$')

    # Define second panel
    plt.subplot(1, 2, 2)
    plt.plot(v, x, 'k')
    plt.axis('equal')

    # this will save the figure as a PDF in the directory you're running it from: is that what you want?
    plt.savefig('Solution-and-Phase.pdf', bbox_inches='tight')

