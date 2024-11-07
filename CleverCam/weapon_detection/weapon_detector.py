from ultralytics import YOLO

class WeaponDetector:
    def __init__(self, model_path):
        # Load the YOLO model for weapon detection
        self.model = YOLO(model_path)

    def detect_weapons(self, frame):
        # Run detection on the frame
        results = self.model(frame)
        
        # Assuming weapon-related classes are at indices 0, 1, and 2 for gun, knife, and blade
        threat_indices = [0, 1, 2]
        weapon_detections = [det for det in results[0].boxes if det.cls in threat_indices]
        
        # Check if any weapon is detected
        weapon_detected = len(weapon_detections) > 0
        return weapon_detected, weapon_detections
