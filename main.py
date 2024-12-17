"""main.py"""
import cv2
from ultralytics import YOLO
import easyocr

model = YOLO('best.pt')
reader = easyocr.Reader(['en'], gpu=True)

cap = cv2.VideoCapture(1) # To open the external camera


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Check the IP Camera URL.")
        break

    results = model.predict(source=frame, conf=0.5, save=False, show=False)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0]) 
        conf = box.conf[0]  
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        plate_image = frame[y1:y2, x1:x2]

        ocr_result = reader.readtext(plate_image)
        plate_text = " ".join([text[1] for text in ocr_result]) if ocr_result else "Unknown"

        class_label = f"{class_name} ({conf:.2f})"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, class_label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        ocr_label = f"Text: {plate_text}"
        cv2.putText(frame, ocr_label, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.imshow("Real-time License Plate Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()