import cv2
from ultralytics import YOLO

img = cv2.imread("test.jpeg")
model = YOLO("runs\\detect\\train\\weights\\best.pt")
data = model.predict(img)[0]
for box in data.boxes:
  conf = float(box.conf[0])
  if conf > 0.5:
    name = data.names[int(box.cls)]
    x,y,w,h = [ int(p) for p in box.xywh[0]]
    x1,y1,x2,y2 = [ int(p) for p in (x-w/2,y-h/2,x+w/2,y+h/2)]
    cv2.rectangle(img, (x1,y1),(x2,y2),(0,0,255),1)
    #这儿只是因为显示了看不见，所以图够大，字太上，下移一下
    if y1< 30 and img.shape[0]>100:
      y1 = 30    
    cv2.putText(img,"{:.4f}".format(conf),(x1,y1),1,1,(0,0,255),1)

win_name = "findgirl"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
cv2.imshow(win_name,img)
cv2.waitKey(0)
cv2.destroyAllWindows()