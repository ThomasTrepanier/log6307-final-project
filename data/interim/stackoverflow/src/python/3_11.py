# run as
# pytest test_plotting.py

from matplotlib import pyplot as plt


def plot_fn():
    plt.plot([1,2,3])
    plt.show()
    assert False # to check that the code gets here

def test_plot_fn():
    with plt.ion():
        plot_fn()
