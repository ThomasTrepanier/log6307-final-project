import pytest 
import matplotlib.pyplot as plt 

@pytest.fixture(scope='function')
def plot_fn():
    def _plot(points):
        plt.plot(points)
        yield plt.show()
        plt.close('all')
    return _plot


def test_plot_fn(plot_fn):
    points = [1, 2, 3]
    plot_fn(points)
    assert True
