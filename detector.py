import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

clasificacion = cv2.CascadeClassifier('randall/classifier/cascade.xml')

while True:

  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  toy = clasificacion.detectMultiScale(gray,
  scaleFactor = 1.3, 
  minNeighbors = 91,
  minSize = (70, 78))

  for (x, y, w, h) in toy:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, 'Randall Boggs', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) == 27:
    break

cap.release()
cv2.destroyAllWindows()