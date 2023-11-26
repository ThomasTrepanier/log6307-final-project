class MFCC(Spec):

    mfcc: np.ndarray  # Mel-frequency cepstral coefficient
    delta_mfcc: np.ndarray  # delta Mel-frequency cepstral coefficient
    delta2_mfcc: np.ndarray  # delta2 Mel-frequency cepstral coefficient
    n_mfcc: int = 13

    def __init__(self, soundFile: str):
        self.name = path.basename(soundFile)
        self.y, sr = librosa.load(soundFile, sr=self.sr) # <--- This line is changed
        self.mfcc = librosa.feature.mfcc(self.y, n_mfcc=self.n_mfcc, sr=sr)
        self.delta_mfcc = librosa.feature.delta(self.mfcc, mode="nearest")
        self.delta2_mfcc = librosa.feature.delta(self.mfcc, mode="nearest", order=2)
