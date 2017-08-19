import cv2
import sys
import numpy


classifier = cv2.CascadeClassifier('./classifier/cascade.xml')

def main():

    img = cv2.imread('../test.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = classifier.detectMultiScale(gray, 1.10, 10)

    for (x,y,w,h) in cars:
        cv2.drawMarker(img=img, position=(x, y), markerType=cv2.MARKER_CROSS,color=(0, 0, 0), thickness=2, line_type=cv2.LINE_AA, markerSize=20)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img=img,text='CAR',org=(x + w/2, y + h/2), fontFace=font, fontScale=1, color=(10, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('HAAR',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()








if __name__ == '__main__':
    main()
