import librosa
import numpy as np
import scipy.signal as signal
import soundfile as sf

input_file = "../data/input.wav"
output_file = "../data/output.wav"

x, fs = librosa.load(input_file, sr=None)

# 1. Define fractional time factor (alpha)
# alpha = 1.2 means y[n] = x[1.2n] (speed up by 1.2x, pitch goes up)
# alpha = 0.8 means y[n] = x[0.8n] (slow down by 1.25x, pitch goes down)
alpha = 1.3

# 2. Calculate new sequence length 
num_samples_new = int(len(x) / alpha)

# 3. Resample (Interpolates non-integer indices mathematically)
y = signal.resample(x, num_samples_new)

# 4. Save output
sf.write(output_file, y, fs)

print(f"Original length: {len(x)} -> Manipulated length: {len(y)}")