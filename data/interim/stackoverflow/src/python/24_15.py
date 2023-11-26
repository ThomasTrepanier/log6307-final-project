def spectra_of_spectra(mfcc):
    # first calculate the psd
    fft = np.fft.fft(mfcc.y)
    fft = fft[:len(fft)//2+1]
    psd1 = np.real(fft * np.conj(fft))
    # then calculate the psd of the psd
    fft = np.fft.fft(psd1/sum(psd1))
    fft = fft[:len(fft)//2+1]
    psd = np.real(fft * np.conj(fft))
    return(np.sum(psd)/len(psd))
