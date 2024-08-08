originalImage = imread('lighthouse.png');

% RGB Image
subplot(2, 2, 1);
imshow(originalImage);
title('Original RGB Image')
% Grayscale Image
grayscaleImage = rgb2gray(originalImage);
subplot(2, 2, 2);
imshow(grayscaleImage);
title('Grayscale Image');

% Rotated Image
rotatedImage = imrotate(originalImage, 45);
subplot(2, 2, 3);
imshow(rotatedImage);
title('Rotated Image');

%The Histogram of the Grayscale Image
subplot(2, 2, 4);
imhist(grayscaleImage);
title('Histogram of Grayscale Image');

