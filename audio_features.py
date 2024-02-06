import librosa
import numpy as np

def extraer_caracteristicas(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    
    # Calcula los coeficientes cepstrales de frecuencia mel
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    # Calcula la energia de espectro
    espectro = np.abs(librosa.stft(y))
    energia = np.mean(librosa.feature.rms(S=espectro))
    
    # Calcula la frecuencia fundamental
    tono, _ = librosa.piptrack(y=y, sr=sr)
    tono_promedio = np.mean(tono)
    
    return mfccs, energia, tono_promedio

audio_file = "/dataset/banana_yo.wav"
mfccs, energia, tono = extraer_caracteristicas(audio_file)

print("MFCCs:", mfccs.shape)
print("Energia del espectro:", energia)
print("Frecuencia fundamental:", tono)