# **AUTOMATIC LICENSE PLATE RECOGNITION (ALPR) FOR INDONESIA PLATE NUMBER USING YOLOv8**


## Domain Project
This project focuses on the development of an Automatic License Plate Recognition (ALPR) system to automatically detect and recognize license plate number. The system develop to support aplication like parking management, traffic control, and law enforcement.

## Problem Statements
1. How can the accuracy of lincese plate detection and recognition be improved using YOLOv8?
2. How can system achieve high-accuracy license plate recognition using EasyOCR?

## Goals
1. Develop a model to accurately detect license plates using YOLOv8.
2. Create a real-time system to detect and recognize text on license plates.

## Solution Statements
1. Train the YOLOv8 model on a custom, high-quality dataset to improve detection accuracy.
2. Integrate EasyOCR with the detection model to recognize text on license plates.

## Data Collection
1. Images of Indonesian license plates were collected from Google.
2. The images were classified into 4 classes: old vehicles with black plates, new vehicles with white plates, electric vehicles, and public transportation.
3. Each image was manually labeled with bounding boxes using the Roboflow platform.
4. You can access the dataset [[HERE]](https://universe.roboflow.com/tes-60jyf/indonesian_plate_detection).

## Modelling
### Plate Detection Task
We used the YOLOv8 model for the license plate detection task. In this task, the YOLOv8 model was trained on 396 images with hyperparameter tuning, such as setting the number of epochs to 200.

### Character Recognition Task
We use EasyOCR to recognition character in plate. 

## Evaluation
| Class            | Precision | Recall | mAP50 | mAP50-95 |
|------------------|-----------|--------|-------|----------|
| all              | 0.981     | 0.972  | 0.988 | 0.942    |
| old vehicle      | 1         | 0.994  | 0.995 | 0.94     |
| new vehicle      | 0.975     | 0.923  | 0.98  | 0.931    |
| electric vehicle | 0.996     | 1      | 0.995 | 0.939    |
| public transport | 0.951     | 0.972  | 0.981 | 0.959    |

## Recommendation
1. Enhance the dataset: Collect more images from diverse sources to increase robustness.
2. Consider using attention-based models like Vision Transformers (ViT) to achieve higher accuracy.

