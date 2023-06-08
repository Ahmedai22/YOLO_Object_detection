import cv2
from ultralytics import YOLO

# Load the object detection model
model = YOLO('../yolo_weights/yolov8l.pt')

# Access the video stream
video_stream = cv2.VideoCapture(0)  # Use 0 for webcam, or specify the path to a video file

while True:
    # Read the next frame
    ret, frame = video_stream.read()
    if not ret:
        break

    # Perform object detection on the frame
    detections = model(frame)

    # Draw boxes on the detected objects
    for bbox in detections:
        x, y, width, height = bbox
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)  # Green rectangle with thickness 2

    # Display the annotated frame
    cv2.imshow('Object Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video stream and close windows
video_stream.release()
cv2.destroyAllWindows()



