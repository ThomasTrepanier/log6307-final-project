import numpy as np
from scipy import fftpack as scipy_fftpack
from scipy import fft as scipy_fft


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

print('\n####################     INPUT DATA     ###################\n')

# initialize two 2D arrays with random data for testing
in1 = np.array([[0,   0,   0,   0], \
                [0, 255, 255,   0], \
                [0,   0, 255, 255], \
                [0,   0,   0,   0]])

print('\nin1 shape=', in1.shape, '\n', in1)

in2 = np.array([[0,   0,   0,   0], \
                [0,   0, 255,   0], \
                [0, 255, 255,   0], \
                [0, 255,   0,   0]])

print('\nin2 shape=', in2.shape, '\n', in2)

print('\n###############    SCIPY: 2D RFFT (MULT)    ###############\n')

# transform both inputs with SciPy RFFT for 2D
scipy_rfft1 = scipy_fft.fftn(in1)
scipy_rfft2 = scipy_fft.fftn(in2)

print('* Output from scipy_fft.rfftn():')
print('scipy_fft1 shape=', scipy_rfft1.shape, '\n', scipy_rfft1)
print('\nscipy_fft2 shape=', scipy_rfft2.shape, '\n', scipy_rfft2)

# perform multiplication between two 2D arrays from SciPy RFFT
scipy_rfft_mult = scipy_rfft1 * scipy_rfft2

# perform inverse RFFT for 2D arrays using SciPy
scipy_data = scipy_fft.irfftn(scipy_rfft_mult, in1.shape) # passing shape guarantees the output will
                                                          # have the original data size
print('\n* Output from scipy_fft.irfftn():')
print('scipy_data shape=', scipy_data.shape, '\n', scipy_data)

print('\n###############   FFTPACK: 2D RFFT (MULT)   ###############\n')

# transform both inputs with FFTPACK RFFT for 2D
fftpack_rfft1 = fftpack_rfft2d(in1)
fftpack_rfft2 = fftpack_rfft2d(in2)
print('* Output from fftpack_rfft2d():')
print('fftpack_rfft1 shape=', fftpack_rfft1.shape, '\n', fftpack_rfft1)
print('\nfftpack_rfft2 shape=', fftpack_rfft2.shape, '\n', fftpack_rfft2)

# TODO: perform multiplication between two 2D arrays from FFTPACK RFFT
fftpack_rfft_mult = fftpack_rfft1 * fftpack_rfft2 # this doesn't work

# perform inverse RFFT for 2D arrays using FFTPACK
fftpack_data = fftpack_irfft2d(fftpack_rfft_mult)
print('\n* Output from fftpack_irfft2d():')
print('fftpack_data shape=', fftpack_data.shape, '\n', fftpack_data)

print('\n#####################      RESULT     #####################\n')

# compare FFTPACK result with SCIPY
print('\nIs fftpack_data equivalent to scipy_data?', np.allclose(fftpack_data, scipy_data), '\n')
