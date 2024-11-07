from ultralytics import YOLO

class CrowdDetector:
    def __init__(self, model_path, crowd_threshold=10):
        # Load the YOLO model for crowd detection
        self.model = YOLO(model_path)
        self.crowd_threshold = crowd_threshold  # Set threshold for crowd detection

    def detect_crowd(self, frame):
        # Run detection on the frame    
        results = self.model(frame)
        # Filter for 'person' detections (class 0 in COCO)
        person_detections = [det for det in results[0].boxes if det.cls == 0]
        # Check if the number of people exceeds the crowd threshold
        crowd_detected = len(person_detections) >= self.crowd_threshold
        return crowd_detected, person_detections
