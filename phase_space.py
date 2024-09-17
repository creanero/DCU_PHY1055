import matplotlib.pyplot as plt

# when you merge this into R3_template, you will use the values of v and x in that program
v = []
x = []

plt.figure()

# plots v against x in black ('k')
plt.plot(v, x, 'k')

# sets the axes to equal sizes
plt.axis('equal')

# labels the axes
plt.xlabel(r"$x$")
plt.ylabel(r"$v$")