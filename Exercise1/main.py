import librosa

wave_files = [
    "Exercise1/speech1.wav",
    "Exercise1/speech2.wav"
]

"""
1a) What is the sampling frequency of the signals?
"""
def get_sampling_freq(path):
    _, sampling_rate = librosa.load(path)
    print(f"The sampling frequency of file '{path}' is: {sampling_rate} Hz.")

for file in wave_files:
    get_sampling_freq(file)

"""
b) Plot the signal as a function of time [s]. For this, create a vector which contains the time instants for each
sample. For plotting, you can employ the plot command from matplotlib.pyplot
•Identify the voiced, unvoiced and silence regions in the waveform. Which criteria did you use to
distinguish between the three signal types?
"""
