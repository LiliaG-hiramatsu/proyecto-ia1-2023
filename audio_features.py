import librosa

import numpy as np
import pandas as pd

from glob import glob

import matplotlib.pylab as plt
import seaborn as sns

import librosa.display

from itertools import cycle


data_dir = './dataset'
audio_files = glob(data_dir + '/*.wav')

y, sr = librosa.load(audio_files[0]) #sr=sample rate (frecuencia de muestreo)
#print(f'y: {y[:10]}')
#print(f'shape y: {y.shape}')
#print(f'sr: {sr}')

#pd.Series(y).plot(figsize=(10, 5), lw=1, title='Raw Audio Example')
#plt.show()

#y_trimmed, _ = librosa.effects.trim(y, top_db=20)
#pd.Series(y_trimmed).plot(figsize=(10, 5), lw=1, title='Raw Audio Trimmed Example')
#plt.show()

#pd.Series(y[9500:10000]).plot(figsize=(10, 5), lw=1, title='Raw Audio Zoomed In Example')
#plt.show()

# Spectogram
#D = librosa.stft(y)
#S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
#print(S_db.shape)

#fig, ax = plt.subplots(figsize=(10, 5))
#img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
#ax.set_title('Spectogram Example', fontsize=20)
#fig.colorbar(img, ax=ax, format=f'%0.2f')
#plt.show()

# Mel Spectogram

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128*2)
S_db_mel = librosa.amplitude_to_db(S, ref=np.max)

fig, ax = plt.subplots(figsize=(10, 5))
img = librosa.display.specshow(S_db_mel, x_axis='time', y_axis='log', ax=ax)
ax.set_title('Mel Spectogram Example', fontsize=20)
fig.colorbar(img, ax=ax, format=f'%0.2f')
plt.show()

'''
for file in range(0, len(audio_files), 1):
    audio, sfreq = librosa.load(audio_files[file])
    time = np.arange(0, len(audio)) / sfreq
    
    # Plot audio over time
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
    plt.show()
'''