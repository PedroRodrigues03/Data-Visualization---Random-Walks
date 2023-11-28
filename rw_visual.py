import matplotlib.pyplot as plt

from random_walk import RandomWalk


if __name__ == "__main__":
    # Make random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('grayscale')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.savefig('random_walk_plot.png', bbox_inches='tight')
