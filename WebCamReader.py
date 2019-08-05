import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)



while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    canny = cv2.Canny(blur, 50,150)

    plt.imshow('result',canny)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
plt.destroyAllWindows()
