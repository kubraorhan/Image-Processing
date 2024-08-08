# Hatice Kübra Orhan - 200316006
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# Load the initial image in grayscale
initial_image = cv2.imread('image78.png', cv2.IMREAD_GRAYSCALE)

# Perform Fourier transform
fourier_spectrum = np.fft.fft2(initial_image)
shifted_fourier_spectrum = np.fft.fftshift(fourier_spectrum)
magnitude_spectrum = 20 * np.log(np.abs(shifted_fourier_spectrum))

# Define points and radius
point1 = (120, 120)
point2 = (136, 136)
radius = 6

# Zero out the specified areas in the Fourier spectrum
for i in range(-radius, radius + 1):
    for j in range(-radius, radius + 1):
        shifted_fourier_spectrum[point1[0] + i, point1[1] + j] = 0
        shifted_fourier_spectrum[point2[0] + i, point2[1] + j] = 0

# Perform the inverse Fourier transform
filtered_spectrum = np.fft.ifftshift(shifted_fourier_spectrum)
inverse_filtered_spectrum = np.fft.ifft2(filtered_spectrum)
filtered_image = np.abs(inverse_filtered_spectrum)

# Median filter function
def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

# Apply median filter to the filtered image
removed_noise = median_filter(filtered_image, 3)

# Plotting
plt.figure(figsize=(18, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(initial_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Fourier Spectrum
plt.subplot(1, 3, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Spectrum')
plt.axis('off')

# Filtered Image
plt.subplot(1, 3, 3)
plt.imshow(removed_noise, cmap='gray')
plt.title('Final result')
plt.axis('off')

plt.tight_layout()
plt.show()
