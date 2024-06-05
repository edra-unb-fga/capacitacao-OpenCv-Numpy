import cv2
import numpy as np 

def colorDetection(frame, lower, upper, ColorName):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    #countour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        if cv2.contourArea(contour) > 200:  # Filtrar pequenos contornos
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, ColorName, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

lower_red = np.array([0, 150, 150])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = colorDetection(frame, lower_red, upper_red, "RED")
    frame = colorDetection(frame, lower_blue, upper_blue, "blue")
    
    cv2.imshow("Original", frame)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
