import random
import cv2 as cv
import numpy as np

def add_gaussian_noise(img, sigma, mean):
    row, col = img.shape

    gaussian_noise = np.random.normal(mean, sigma, (row, col)).reshape(row, col)
    noisy_img = img + gaussian_noise

    noisy_img = np.clip(noisy_img, 0, 255) # Alle tal er mellem 0 og 255

    return noisy_img.astype(np.uint8) # Afrunder eventuelle floats og ændre til integers

img_bgr = cv.imread(r"Lektion 3\image.png")
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
sigma_value = 25 # Sigma er en brugerparameter
mean = 0 # mean er 0
img_gaussian_noise = add_gaussian_noise(img_gray, sigma_value)

kernel_size = (3, 3)
img_filtered = cv.blur(img_gaussian_noise, kernel_size)
img_median_filtered = cv.medianBlur(img_gaussian_noise, 3)

cv.imwrite(r'Lektion 3\img_gray.jpg', img_gray)
cv.imwrite(r'Lektion 3\img_gaussian_noise.jpg', img_gaussian_noise)
cv.imwrite(r'Lektion 3\img_filtered_gas.jpg', img_filtered)
cv.imwrite(r'Lektion 3\img_median_filtered_gas.jpg', img_median_filtered)

cv.imshow('Original Gray', img_gray)
cv.imshow('Gaussian Noise Added', img_gaussian_noise)
cv.imshow('Mean Filtered', img_filtered)
cv.imshow('Median Filtered', img_median_filtered)
cv.waitKey(0)
cv.destroyAllWindows()
