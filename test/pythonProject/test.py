import cv2
import pytesseract
from PIL import Image
from imutils import contours
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_CONTRAST, 200)  #200
cap.set(cv2.CAP_PROP_FPS, 24)

while(True):
    ret, frame = cap.read()
    height, width, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts, _ = contours.sort_contours(cnts[0])

    cv2.imshow('frame', thresh)
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        if area > 5000:
            img = frame[y:y+h, x:x+w]
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            result = pytesseract.image_to_string(img, lang="rus+eng")

            s = result
            if len(s) > 7:
                print(s.upper())
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()


