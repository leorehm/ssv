import librosa

wave_files = [
    "Exercise1/speech1.wav",
    "Exercise1/speech2.wav"
]

# 1a) What is the sampling frequency of the signals?
def get_sampling_freq(path):
    _, sampling_rate = librosa.load(path)
    print(f"The sampling frequency of file '{path}' is: {sampling_rate} Hz.")

for file in wave_files:
    get_sampling_freq(file)
