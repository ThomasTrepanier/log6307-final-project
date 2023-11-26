import pytest
import unittest
try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch


@patch("methylcheck.qc_plot.plt.show")
def test_plot_fn(mock_this):
   plot_fn()
   plt.close('all')
