from unittest.mock import patch 
import pytest 
import matplotlib.pyplot as plt 

def plot_fn():
    plt.plot([1,2,3])
    plt.show()

@patch("matplotlib.pyplot.show")
def test_plot_fn(mock_show):
    plot_fn()
