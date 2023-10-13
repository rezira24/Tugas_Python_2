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

def fft2D(matrix):
    # FFT pada setiap baris
    rows = [fft(row) for row in matrix]
    
    # FFT pada setiap kolom
    cols = [fft([row[i] for row in rows]) for i in range(len(matrix[0]))]
    
    return cols

# Membuat matriks 2D sebagai contoh (gambar sederhana)
N = 64  # Ukuran gambar
image = [[0.0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        image[i][j] = cmath.sin(5 * 2.0 * cmath.pi * i / N) + cmath.sin(5 * 2.0 * cmath.pi * j / N)

# Melakukan FFT 2D menggunakan implementasi sendiri
fft_result = fft2D(image)

# Mengambil amplitudo (magnitude) FFT 2D
magnitude = [[abs(val) for val in row] for row in fft_result]

# Plot spektrum frekuensi dengan map warna berbeda
plt.figure(figsize=(8, 6))
plt.imshow(magnitude, cmap='jet')  # Ganti 'jet' dengan map warna lain (e.g., 'viridis', 'plasma')
plt.title("Spektrum Frekuensi Gambar")
plt.colorbar()
plt.show()
