# CleverCam: AI-based Surveillance System

CleverCam is an AI-powered surveillance system designed for real-time monitoring and detection of crowds and weapons. It uses YOLOv8 for object detection, including the ability to detect specific objects such as weapons and crowded scenes. This system automates alerts, making it highly efficient for security applications in high-risk areas.

## Project Structure

The project is organized as follows:

```plaintext
CleverCam/
├── crowd_detection/
│   ├── models/
│   │   └── yolov8n.pt                      # Pre-trained YOLOv8 model for crowd detection (COCO)
│   └── crowd_detector.py                   # Code for detecting crowd in a frame
├── weapon_detection/
│   ├── models/
│   │   └── best.pt                         # Trained YOLOv8 model for weapon detection
│   ├── weapon_detector.py                  # Code for detecting weapons in a frame
│   └── training_results/
│       ├── weights/
│       │   ├── best.pt                     # Best model after training
│       │   └── last.pt                     # Last model after training
│       ├── confusion_matrix.png            # Confusion matrix for weapon detection
│       ├── F1_curve.png                    # F1 score curve
│       ├── P_curve.png                     # Precision curve
│       ├── PR_curve.png                    # Precision-Recall curve
│       ├── R_curve.png                     # Recall curve
│       ├── labels_correlogram.jpg          # Label correlations
│       ├── labels.jpg                      # Label mapping image
│       ├── results.png                     # Graphs showing training results
│       ├── results.csv                     # Training results in CSV format
│       ├── train_batch0.jpg                # Sample training batch images
│       ├── train_batch1.jpg
│       ├── train_batch2.jpg
│       ├── val_batch0_labels.jpg           # Validation batch labels
│       ├── val_batch1_labels.jpg
│       ├── val_batch2_labels.jpg
│       ├── val_batch0_pred.jpg             # Validation batch predictions
│       ├── val_batch1_pred.jpg
│       └── val_batch2_pred.jpg
├── alert_system/
│   └── alert.py                            # Script for sending alerts
├── main.py                                 # Main program to integrate crowd and weapon detection with alert system
├── config.yaml                             # Configuration file for parameters like threshold values
├── requirements.txt                        # Dependencies for the project
└── README.md
```

## Usage

- **Crowd Detection**: Run `crowd_detector.py` to detect crowds in a video frame.
- **Weapon Detection**: Run `weapon_detector.py` to detect weapons in a video frame.
- **Alert System**: Use `alert.py` to set up alerts that trigger upon detection.

## Configuration

- You can adjust the detection thresholds and other parameters in `config.yaml`.
- The results from training, including confusion matrices and precision-recall curves, are available in the `training_results` directory under `weapon_detection/`.
ection
