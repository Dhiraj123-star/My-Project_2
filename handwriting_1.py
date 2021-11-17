# change any text into handwritten text using Python

import pywhatkit as kit


import cv2

kit.text_to_handwriting("Python is very famous programming language available in the market",
save_to="handwriting_1.png")

img = cv2.imread('handwriting_1.png')

cv2.imshow("text_handwritten_",img)

cv2.waitKey(0)

cv2.destroyAllWindows()