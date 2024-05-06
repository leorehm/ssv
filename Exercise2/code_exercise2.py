import numpy as np


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
) -> [np.ndarray]:
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


def compute_stft(
    v_signal: np.ndarray,
    fs: int,
    frame_length: int,
    frame_shift: int,
    v_analysis_window: np.ndarray,
):

    samples_per_frame = int(fs * frame_length / 1000)
    samples_per_shift = int(fs * frame_shift / 1000)

    if len(v_analysis_window) != samples_per_frame:
        raise ValueError("v_analysis_window invalid length")
    # 1. Split the time domain signal into overlapping blocks
    m_frames, v_time_frames = my_windowing(v_signal, fs, frame_length, frame_shift)
    # 2. Apply the analysis window to each segment of the time domain signal
    m_frames = m_frames * v_analysis_window  # ifftshift ?
    # 3. Use the fft function provided by np.fft to compute the DFT for each windowed segment
    dft = np.fft.fft(m_frames, axis=1)
    # 4. Only keep the lower half of the spectrum and remove the upper half. Make sure that the frequency bin at the Nyquist frequency is still included

    return None
