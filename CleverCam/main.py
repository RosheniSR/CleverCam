import cv2
import yaml
import time
from crowd_detection.crowd_detector import CrowdDetector
from weapon_detection.weapon_detector import WeaponDetector
from alert_system.alert import AlertSystem

# Load configuration
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize detectors and alert system
crowd_detector = CrowdDetector(
    model_path=config['crowd_detection']['model_path'],
    crowd_threshold=config['crowd_detection']['threshold']
)
weapon_detector = WeaponDetector(model_path=config['weapon_detection']['model_path'])

alert_system = AlertSystem(
    account_sid=config['alert_system']['account_sid'],
    auth_token=config['alert_system']['auth_token'],
    twilio_number=config['alert_system']['twilio_number'],
    receiver_whatsapp_number=config['alert_system']['receiver_whatsapp_number']
)

# Set cooldown period in seconds
alert_cooldown = 30
last_crowd_alert_time = 0
last_weapon_alert_time = 0

# Process video for crowd detection
video_path = config['crowd_detection']['video_path']  # Path to the crowd detection video
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    # Check for crowd detection with cooldown
    crowd_detected, person_detections = crowd_detector.detect_crowd(frame)
    if crowd_detected and (current_time - last_crowd_alert_time > alert_cooldown):
        alert_system.send_alert("Crowd Detected", "A crowd has been detected by CleverCam.")
        last_crowd_alert_time = current_time  # Update the last alert time for crowd

    # Display frame (optional for debugging)
    cv2.imshow('Crowd Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Process image for weapon detection
image_path = config['weapon_detection']['image_path']  # Path to the weapon detection image
image = cv2.imread(image_path)

if image is not None:
    weapon_detected, weapon_detections = weapon_detector.detect_weapons(image)
    # Only send alert for weapon detection if cooldown period has passed
    if weapon_detected and (time.time() - last_weapon_alert_time > alert_cooldown):
        alert_system.send_alert("Weapon Detected", "A potential weapon has been detected by CleverCam.")
        last_weapon_alert_time = time.time()  # Update the last alert time for weapon detection

    # Display image with weapon detection results (optional for debugging)
    cv2.imshow('Weapon Detection', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
