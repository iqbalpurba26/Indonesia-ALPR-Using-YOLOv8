# -*- coding: utf-8 -*-
"""Automatic License Plate Recognition For Indonesia Plate Number.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D4LYy4CzTwRKgU9mNBBMsRpRRjxvcrN9

# **AUTOMATIC LICENSE PLATE RECOGNITION FOR INDONESIA PLATE NUMBER**

## **INSTALL AND IMPORT LIBRARY**
"""

!pip -q install git+https://github.com/ultralytics/ultralytics.git roboflow

from roboflow import Roboflow
from ultralytics import YOLO
import pandas as pd
from IPython.display import Image, display
import numpy as np

"""## **DOWNLOAD DATASET FROM ROBOFLOW**"""

rf = Roboflow(api_key="1E5IZ1OwAOeeAhHYF6HD")
project = rf.workspace("tes-60jyf").project("indonesian_plate_detection")
version = project.version(2)
dataset = version.download("yolov8")

"""## **MODEL TRAINING**"""

model = YOLO("yolov8n.pt")

model.train(
    data = "/content/indonesian_plate_detection-2/data.yaml",
    epochs = 200,
)

"""## **EVALUATION**"""

results = model.val()

df_results = pd.read_csv('/content/runs/detect/train/results.csv')
df_results

display(Image('/content/runs/detect/train/results.png'))