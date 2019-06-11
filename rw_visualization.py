import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk and plot the points
rw = RandomWalk()
rw.fill_walk()

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Customize our plots to create colormap to show the order of the
    # points, remove the black outline from each dot.  To color the
    # points pass the c argument contianing position of each point.
    # Use the Blues colormap, edgecolor='none' to remove the outline
    # around each point.  
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)
    # Emphasize the first and last points.
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors = 'none', s=100)
    plt.show()

    keep_running = input("Make another random walk? (y/n): ")
    if keep_running == 'n':
        break
    
