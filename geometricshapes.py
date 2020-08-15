import cv2
import numpy as np
#image = cv2.imread('lena.jpg', 1)
image = np.zeros([512, 512, 3], np.uint8)  # creating an image
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 5)
image = cv2.arrowedLine(image, (0, 255), (255, 255), (255, 0, 0), 5)
image = cv2.rectangle(image, (384, 0), (510, 128), (0, 0, 255), 10)
image = cv2.circle(image, (447, 63), 63, (0, 255, 0), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, 'opencv', (10, 500), font, 4,
                    (0, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
