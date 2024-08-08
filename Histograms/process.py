from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

original_image = Image.open('lighthouse.png')

# RGB Image
plt.subplot(2, 2, 1)
plt.imshow(np.array(original_image))
plt.title('Original RGB Image')

# Grayscale Image
grayscale_image = original_image.convert('L')
plt.subplot(2, 2, 2)
plt.imshow(np.array(grayscale_image), cmap='gray')
plt.title('Grayscale Image')

# Rotated Image
rotated_image = original_image.rotate(45)
plt.subplot(2, 2, 3)
plt.imshow(np.array(rotated_image))
plt.title('Rotated Image')

# The Histogram of the Grayscale Image
plt.subplot(2, 2, 4)
plt.hist(np.array(grayscale_image).ravel(), bins=256, color='gray', histtype='step')
plt.title('Histogram of Grayscale Image')

plt.show()

