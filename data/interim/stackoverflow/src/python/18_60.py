# Plot audio with zoomed in y axis
def plotAudio(output):
    fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(20,10))
    plt.plot(output, color='blue')
    ax.set_xlim((0, len(output)))
    ax.margins(2, -0.1)
    plt.show()

# Plot audio
def plotAudio2(output):
    fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(20,4))
    plt.plot(output, color='blue')
    ax.set_xlim((0, len(output)))
    plt.show()

def minMaxNormalize(arr):
    mn = np.min(arr)
    mx = np.max(arr)
    return (arr-mn)/(mx-mn)

def predictSound(X):
    clip, index = librosa.effects.trim(X, top_db=20, frame_length=512, hop_length=64) # Empherically select top_db for every sample
    stfts = np.abs(librosa.stft(clip, n_fft=512, hop_length=256, win_length=512))
    stfts = np.mean(stfts,axis=1)
    stfts = minMaxNormalize(stfts)
    result = model.predict(np.array([stfts]))
    predictions = [np.argmax(y) for y in result]
    print(lb.inverse_transform([predictions[0]])[0])
    plotAudio2(clip)

CHUNKSIZE = 22050 # fixed chunk size
RATE = 22050

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, 
rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

#preprocessing the noise around
#noise window
data = stream.read(10000)
noise_sample = np.frombuffer(data, dtype=np.float32)
print("Noise Sample")
plotAudio2(noise_sample)
loud_threshold = np.mean(np.abs(noise_sample)) * 10
print("Loud threshold", loud_threshold)
audio_buffer = []
near = 0

while(True):
    # Read chunk and load it into numpy array.
    data = stream.read(CHUNKSIZE)
    current_window = np.frombuffer(data, dtype=np.float32)
    
    #Reduce noise real-time
    current_window = nr.reduce_noise(audio_clip=current_window, noise_clip=noise_sample, verbose=False)
    
    if(audio_buffer==[]):
        audio_buffer = current_window
    else:
        if(np.mean(np.abs(current_window))<loud_threshold):
            print("Inside silence reign")
            if(near<10):
                audio_buffer = np.concatenate((audio_buffer,current_window))
                near += 1
            else:
                predictSound(np.array(audio_buffer))
                audio_buffer = []
                near
        else:
            print("Inside loud reign")
            near = 0
            audio_buffer = np.concatenate((audio_buffer,current_window))

# close stream
stream.stop_stream()
stream.close()
p.terminate()
