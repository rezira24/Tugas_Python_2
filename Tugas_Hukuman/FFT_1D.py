import cmath
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Membuat sinyal periodik sebagai contoh
N = 256  # Jumlah sampel
T = 1.0 / 800.0  # Interval waktu
x = [0.0] * N
for i in range(N):
    x[i] = 0.5 * (cmath.sin(50.0 * 2.0 * cmath.pi * i * T) + cmath.sin(80.0 * 2.0 * cmath.pi * i * T))

# Melakukan FFT menggunakan implementasi sendiri
fft_result = fft(x)

# Mengambil amplitudo (magnitude) FFT
magnitude = [abs(val) for val in fft_result]

# Membentuk array frekuensi
freq = [i / T for i in range(N)]

# Plot hasil
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot([i.real for i in x])
plt.title("Sinyal Input")

plt.subplot(2, 1, 2)
plt.plot(freq, magnitude)
plt.title("Hasil FFT (Amplitudo)")
plt.xlim(0, 100)  # Menampilkan hanya frekuensi positif

plt.tight_layout()
plt.show()
