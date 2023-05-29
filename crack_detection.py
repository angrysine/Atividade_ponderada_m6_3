# import opencv, yolo
import cv2
from ultralytics import YOLO
from os import listdir

#we get the trained model
model = YOLO("./model.pt")
test_images = [file for file in listdir("./test_images")]
saved_images = []



for image in test_images:
    imS = cv2.resize(cv2.imread(f"./test_images/{image}"), (960, 540)) 
    results = model.predict(imS, conf=0.45)

   
   
    cv2.imshow("show",results[0].plot())
    if cv2.waitKey(0) & 0xFF == ord('a'):
        break

    cv2.destroyAllWindows()
    

  
