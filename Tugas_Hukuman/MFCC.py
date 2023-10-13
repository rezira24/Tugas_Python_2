import matplotlib.pyplot as plt
import math

# Contoh sinyal audio (misalnya, satu jendela data)
sample_rate = 44100  # Frekuensi sampel (Hz)
duration = 0.025  # Durasi jendela (25 ms)
n_samples = int(sample_rate * duration)

# Membuat sinyal audio contoh (misalnya, sinus)
t = [i / sample_rate for i in range(n_samples)]
signal = [math.sin(2 * math.pi * 440 * ti) for ti in t]

# FFT pada jendela data
n_fft = 512
spectrum = [0] * n_fft
for k in range(n_fft):
    for n in range(n_samples):
        spectrum[k] += signal[n] * math.cos(2 * math.pi * k * n / n_samples)

# Mengambil amplitudo spektrum
magnitude = [abs(s) for s in spectrum]

# Plot spektrum frekuensi
plt.figure(figsize=(8, 6))
plt.plot(magnitude)
plt.title("Spektrum Frekuensi Sinyal")
plt.xlabel("Frekuensi (Hz)")
plt.show()