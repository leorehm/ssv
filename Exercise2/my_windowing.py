import numpy as np


def my_windowing(
    v_signal: np.ndarray, sampling_rate: int, frame_length: int, frame_shift: int
) -> tuple[np.ndarray, np.ndarray]:
    samples_per_frame = int(sampling_rate * frame_length / 1000)
    samples_per_shift = int(sampling_rate * frame_shift / 1000)

    N = len(v_signal)
    num_frames = int(np.ceil((N - samples_per_frame) / samples_per_shift)) + 1

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
