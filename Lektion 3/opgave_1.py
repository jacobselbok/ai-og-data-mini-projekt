import random 
import cv2 as cv
  
def add_noise(img): 
    row, col = img.shape 
    total_pixels = row * col
    number_of_pixels = int(total_pixels * 0.1)

    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1) 
        img[y_coord][x_coord] = 255

    number_of_pixels = int(total_pixels * 0.1)
    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1) 
        img[y_coord][x_coord] = 0
          
    return img 

img_bgr = cv.imread(r"Lektion 3\image.png")
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
img_salt_pepper = img_gray.copy()
add_noise(img_salt_pepper)

kernel_size = (3, 3)
img_filtered = cv.blur(img_salt_pepper, kernel_size)
img_median_filtered = cv.medianBlur(img_salt_pepper, 3)

cv.imwrite(r'Lektion 3\img_gray.jpg', img_gray)
cv.imwrite(r'Lektion 3\img_salt_pepper.jpg', img_salt_pepper)
cv.imwrite(r'Lektion 3\img_filtered_sp.jpg', img_filtered)
cv.imwrite(r'Lektion 3\img_median_filtered_sp.jpg', img_median_filtered)

cv.imshow('Gray', img_gray)
cv.imshow('Salt and Pebber', img_salt_pepper)
cv.imshow('Mean Filtered', img_filtered)
cv.imshow('Median Filtered', img_median_filtered)
cv.waitKey(0)
cv.destroyAllWindows()