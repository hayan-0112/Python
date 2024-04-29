import cv2
import numpy as np

net=cv2.dnn.readNet("yolov3_training_final (2).weights","yolov3_testing.cfg")
classes=[]
with open("obj.names", "r") as f:
    classes=[line.strip() for line in f.readlines()]
    print(classes)
layer_names=net.getLayerNames()
output_layers=[layer_names[i-1] for i in net.getUnconnectedOutLayers()]

colors=np.random.uniform(0,255,size=(len(classes),3))

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    frame = cv2.resize(frame,None,fx=1.5,fy=1.5)
    height,width,channels=frame.shape

    blob=cv2.dnn.blobFromImage(frame,0.00392,(416,416),(0,0,0),True,crop=False)
    net.setInput(blob)
    outs=net.forward(output_layers)

    class_ids=[]
    confidences=[]
    boxes=[]
    for out in outs:
        for detection in out:
            scores=detection[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]

            if confidence>0.01:
                center_x = int(detection[0]*width)
                center_y=int(detection[1]*height)
                w=int(detection[2]*width)
                h=int(detection[3]*height)

                x=int(center_x-w/2)
                y=int(center_y-h/2)
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.1,0.1)

    font=cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            label=str(classes[class_ids[i]])
            color=colors[0]
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            cv2.putText(frame,label,(x,y+30),font,3,color,3)

    cv2.imshow("object detection",frame)

    if cv2.waitKey(1)==ord('q'):
        break