import numpy as np
import matplotlib.pyplot as plt

# Helper function for plotting
def plot_signals(t, signals, labels, title):
    plt.figure(figsize=(10, 4))
    for signal, label in zip(signals, labels):
        plt.plot(t, signal, label=label)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# a. Add two sine waves: 5 Hz and 10 Hz, sampled at 1000 Hz for 1 second
fs_a = 1000
t_a = np.linspace(0, 1, fs_a, endpoint=False)
sine_5Hz_a = np.sin(2 * np.pi * 5 * t_a)
sine_10Hz_a = np.sin(2 * np.pi * 10 * t_a)
sum_signal_a = sine_5Hz_a + sine_10Hz_a
plot_signals(t_a, [sum_signal_a], ["5 Hz + 10 Hz Sine"], "a. Sum of 5 Hz and 10 Hz Sine Waves")

# b. Multiply 5 Hz sine and 10 Hz cosine, sampled at 500 Hz for 2 seconds
fs_b = 500
t_b = np.linspace(0, 2, 2 * fs_b, endpoint=False)
sine_5Hz_b = np.sin(2 * np.pi * 5 * t_b)
cosine_10Hz_b = np.cos(2 * np.pi * 10 * t_b)
product_signal_b = sine_5Hz_b * cosine_10Hz_b
plot_signals(t_b, [product_signal_b], ["Sine × Cosine"], "b. Element-wise Product of 5 Hz Sine and 10 Hz Cosine")

# c. Shift 5 Hz sine wave by 0.1 seconds
fs_c = 1000
t_c = np.linspace(0, 1, fs_c, endpoint=False)
sine_5Hz_c = np.sin(2 * np.pi * 5 * t_c)
shifted_t_c = t_c + 0.1
sine_5Hz_shifted_c = np.sin(2 * np.pi * 5 * shifted_t_c)
plot_signals(t_c, [sine_5Hz_c, sine_5Hz_shifted_c], ["Original", "Shifted by 0.1s"], "c. Time-Shifted 5 Hz Sine Wave")

# d. Scale 10 Hz sine wave by factor of 3
fs_d = 1000
t_d = np.linspace(0, 1, fs_d, endpoint=False)
sine_10Hz_d = np.sin(2 * np.pi * 10 * t_d)
scaled_sine_10Hz_d = 3 * sine_10Hz_d
plot_signals(t_d, [sine_10Hz_d, scaled_sine_10Hz_d], ["Original", "Scaled ×3"], "d. Scaled 10 Hz Sine Wave")

# e. Reverse 5 Hz sine wave in time
fs_e = 1000
t_e = np.linspace(0, 1, fs_e, endpoint=False)
sine_5Hz_e = np.sin(2 * np.pi * 5 * t_e)
reversed_sine_5Hz_e = sine_5Hz_e[::-1]
plot_signals(t_e, [sine_5Hz_e, reversed_sine_5Hz_e], ["Original", "Reversed"], "e. Time-Reversed 5 Hz Sine Wave")