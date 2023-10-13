print("Naive Implementation of Convolution")
print("Rezi Rafidan Alfizar")
print("5009211024")

def convolv(signal, conv):
    # Length of the input signal and the convolution kernel
    signal_len = len(signal)
    conv_len = len(conv)

    # Length of the output signal
    output_len = signal_len + conv_len - 1

    # Initialize the output signal as a list of zeros
    output_signal = [0] * output_len

    # Perform convolution
    for i in range(output_len):
        for j in range(conv_len):
            if i - j >= 0 and i - j < signal_len:
                output_signal[i] += signal[i - j] * conv[j]

    return output_signal

# Contoh
signal = [0, 1, 2, 3, 4, 5, 6]
convo = [0, 1, 2, 3]

output_signal = convolv(signal, convo)

# Print the custom convolution result
print("Custom Convolution Result:", output_signal)

# Validate the result using NumPy convolution
import numpy as np

np_convolution = np.convolve(signal, convo, mode='full')

# Print the NumPy result
print("NumPy Convolution Result:", np_convolution)