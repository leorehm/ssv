import numpy as np


# Exercise 2
def my_windowing(
    v_signal: np.ndarray, sampling_rate: int, frame_length: int, frame_shift: int
) -> tuple[np.ndarray, np.ndarray]:
    samples_per_frame = int(sampling_rate * frame_length / 1000)
    samples_per_shift = int(sampling_rate * frame_shift / 1000)

    N = len(v_signal)
    num_frames = int(np.ceil(len(v_signal) / (sampling_rate * frame_shift / 1000)))

    m_frames = np.zeros((num_frames, samples_per_frame))
    v_time_frame = np.zeros(num_frames)

    for i in range(num_frames):
        start = i * samples_per_shift
        end = start + samples_per_frame
        if end <= N:
            m_frames[i, :] = v_signal[start:end]
        else:
            m_frames[i, : N - start] = v_signal[start:N]
        v_time_frame[i] = (start + samples_per_frame / 2) / sampling_rate

    return m_frames, v_time_frame


def compute_stft(
    v_signal: np.ndarray,
    fs: int,
    frame_length: int,
    frame_shift: int,
    v_analysis_window: np.ndarray,
):  # -> [np.ndarray (m_stft), np.ndarray (v_freq), np.ndarray (v_time)]:
    """
    Input:
    - v_signal vector containing the time domain signal
    - fs sampling rate in Hz
    - frame_length frame length in milliseconds
    - frame_shift frame shift in milliseconds
    - v_analysis_window vector that contains the spectral analysis window (This vector should have the same length as the frames, i.e., frame_length in samples.)
    Output:
    - m_stft a matrix which stores the complex short-time spectra in each row
    - v_freq a vector which contains the frequency axis (in units of Hertz) corresponding to the computed spectra
    - v_time time steps around which a frame is centered (as in previous exercise)
    """
    samples_per_frame = int(fs * frame_length / 1000)
    if len(v_analysis_window) != samples_per_frame:
        raise ValueError("v_analysis_window invalid length")

    # 1. Split the time domain signal into overlapping blocks
    m_frames, v_time = my_windowing(v_signal, fs, frame_length, frame_shift)

    # calculate v_freq
    v_freq = fs * (np.arange(samples_per_frame / 2 + 1) / samples_per_frame)

    # 2. Apply the analysis window to each segment of the time domain signal
    m_frames *= v_analysis_window

    # 3. Use the fft function provided by np.fft to compute the DFT for each windowed segment
    dft = np.fft.fft(m_frames, axis=1)

    # 4. Only keep the lower half of the spectrum and remove the upper half
    num_freq_bins = dft.shape[1]
    # Make sure that the frequency bin at the Nyquist frequency is still included
    if num_freq_bins % 2 == 0:  # Even number of bins
        dft = dft[:, : num_freq_bins // 2 + 1]
    else:  # Odd number of bins
        dft = dft[:, : (num_freq_bins + 1) // 2]

    # 5. Store the transformed frames in the rows of the output matrix m_stft
    m_stft = dft

    # Test
    rfft = np.fft.rfft(m_frames, axis=1)
    np.testing.assert_array_almost_equal(m_stft, rfft)

    return m_stft, v_freq, v_time


def convert_to_samples(milliseconds: int, sampling_freq: int):
    """
    Convert a millisecond duration into the number of samples given the sampling frequency.

    :param milliseconds: duration to be converted to number of samples
    :param sampling_freq: the sampling frequency
    :return: number of samples
    """
    return int(milliseconds * (10 ** (-3)) * sampling_freq)


def compute_istft(
    stft: np.ndarray, sampling_rate: int, frame_shift: int, synthesis_window: np.ndarray
) -> np.ndarray:
    """
    Compute the inverse short-time Fourier transform.

    :param stft: STFT transformed signal
    :param sampling_rate: the sampling rate in Hz
    :param frame_shift: the frame shift used to compute the STFT in milliseconds
    :param synthesis_window: a numpy array containing a synthesis window function (length must match with time domain
    signal segments that were used to compute the STFT)
    :return: a numpy array containing the time domain signal
    """

    # compute inverse rFFT and apply synthesis window
    time_frames = np.fft.irfft(stft)
    num_frames, samples_per_frame = time_frames.shape
    assert samples_per_frame == len(
        synthesis_window
    ), "Synthesis window must match the number of samples per frame."
    time_frames *= synthesis_window

    # compute output size
    samples_per_shift = convert_to_samples(frame_shift, sampling_rate)
    output_len = samples_per_frame + (num_frames - 1) * samples_per_shift
    time_signal = np.zeros((output_len))

    # reconstruct signal by adding overlapping windowed segments
    for i in range(num_frames):
        time_signal[
            i * samples_per_shift : i * samples_per_shift + samples_per_frame
        ] += time_frames[i]

    return time_signal
