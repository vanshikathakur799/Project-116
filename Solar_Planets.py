import cv2

image = cv2.imread("solar-system.jpg")

cv2.putText(image, "Sun", (90, 90), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255))
cv2.putText(image, "Mercury", (110, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Venus", (190, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Earth", (290, 265), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Moon", (330, 160), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255))
cv2.putText(image, "Mars", (380, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Jupiter", (490, 70), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Saturn", (715, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Uranus", (965, 135), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image, "Neptune", (1110, 285), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imshow("Planets", image)
cv2.waitKey(0)

cv2.imwrite("Solar_System_withName.jpg", image)

