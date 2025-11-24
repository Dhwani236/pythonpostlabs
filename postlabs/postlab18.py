import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

# --- 1. Load Audio File and Impulse Response ---
# Create dummy audio and impulse response files for demonstration
# In a real scenario, you would load actual .wav files
fs = 44100  # Sample rate
duration = 1.0  # seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
audio_signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t) # Example audio
impulse_response = np.exp(-10 * t) * np.cos(2 * np.pi * 100 * t) # Example impulse

# Normalize for better audio output (optional)
audio_signal = audio_signal / np.max(np.abs(audio_signal))
impulse_response = impulse_response / np.max(np.abs(impulse_response))

# --- 2. Perform Linear Convolution ---
linear_convolved_signal = signal.convolve(audio_signal, impulse_response, mode='full')

# --- 3. Perform Circular Convolution (using FFT) ---
N = len(audio_signal) + len(impulse_response) - 1 # Length for linear convolution
# For circular convolution of a specific length, choose N appropriately
# Here, we'll make it the same length as the linear convolution for direct comparison
# Pad signals to the next power of 2 for efficient FFT
fft_len = int(2**np.ceil(np.log2(N)))

audio_fft = np.fft.fft(audio_signal, fft_len)
impulse_fft = np.fft.fft(impulse_response, fft_len)

circular_convolved_signal_fft = np.fft.ifft(audio_fft * impulse_fft)
circular_convolved_signal = circular_convolved_signal_fft[:N].real # Take real part and truncate

# --- 4. Visualize Results ---
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, audio_signal)
plt.title('Original Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(np.linspace(0, len(linear_convolved_signal)/fs, len(linear_convolved_signal), endpoint=False), linear_convolved_signal)
plt.title('Linear Convolved Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(np.linspace(0, len(circular_convolved_signal)/fs, len(circular_convolved_signal), endpoint=False), circular_convolved_signal)
plt.title('Circular Convolved Signal (FFT-based)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Visualize Spectrograms (optional)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.specgram(linear_convolved_signal, Fs=fs, cmap='viridis')
plt.title('Spectrogram of Linear Convolved Signal')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.subplot(1, 2, 2)
plt.specgram(circular_convolved_signal, Fs=fs, cmap='viridis')
plt.title('Spectrogram of Circular Convolved Signal')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.tight_layout()
plt.show()




