import numpy as np
from scipy import fftpack as scipy_fftpack
from scipy import fft as scipy

# FFTPACK RFFT 2D
def fftpack_rfft2d(matrix):
    fftRows = scipy_fftpack.fft(matrix, axis=1)
    fftCols = scipy_fftpack.fft(fftRows, axis=0)

    return fftCols

# FFTPACK IRFFT 2D
def fftpack_irfft2d(matrix):
    ifftRows = scipy_fftpack.ifft(matrix, axis=1)
    ifftCols = scipy_fftpack.ifft(ifftRows, axis=0)

    return ifftCols.real
