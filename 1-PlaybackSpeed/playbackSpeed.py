import librosa
import soundfile as sf

# 1. Load the .m4a file into discrete signal x[n]
input_file = "input.m4a"
output_file = "output.wav"

x, fs = librosa.load(input_file, sr=None)

# 2. Discrete time manipulation (e.g., y[n] = x[2n])
y = x[::2]

# 3. Export back to file
sf.write(output_file, y, fs)