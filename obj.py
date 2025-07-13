import cv2
from ultralytics import YOLO



model = YOLO("yolo12n.pt") #pre trained model
   
tracking = False
tracker = None

def select_object(event, x, y, flags, param):
    global tracking, tracker, bbox, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        bbox = cv2.selectROI("Select Object", frame, fromCenter=False)
        tracker = cv2.TrackerMOSSE_create() 
        tracker.init(frame, bbox)
        tracking = True


cap = cv2.VideoCapture(0) 
cv2.namedWindow("Live Tracking")
cv2.setMouseCallback("Live Tracking", select_object)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    if tracking:
        success, bbox = tracker.update(annotated_frame)
        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(annotated_frame, "Tracking Failed!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Show live feed
    cv2.imshow("Live Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()