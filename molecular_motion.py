import matplotlib.pyplot as plt
from termcolor import colored

from random_walk import RandomWalk

if __name__ == "__main__":
    mol = RandomWalk(100_000)
    mol.fill_walk()

    plt.style.use('grayscale')
    fig, ax = plt.subplots(figsize=(15,9))
    ax.plot(mol.x_values, mol.y_values, linewidth=1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig('molecular_plot.png', bbox_inches='tight')