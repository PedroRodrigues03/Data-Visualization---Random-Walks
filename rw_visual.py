import matplotlib.pyplot as plt

from random_walk import RandomWalk


if __name__ == "__main__":
    # Keep making new walks, as long as the program is active
    while True:
        # Make random walk
        rw = RandomWalk(50_000)
        rw.fill_walk()

        # Plot the points in the walk
        plt.style.use('grayscale')
        fig, ax = plt.subplots(figsize=(15,9))
        point_numbers = range(rw.num_points)
        ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

        # Emphasize the first and last points
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

        # Remove the axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.savefig('random_walk_plot.png', bbox_inches='tight')

        keep_running = input("Make another wlak? (y/n) ").strip().lower()[0]
        if keep_running == 'n':
            break
