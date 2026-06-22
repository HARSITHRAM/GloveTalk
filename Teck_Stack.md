# GloveTalk: AI-Powered Smart Sign Language Translation Glove

## Project Overview

GloveTalk is a wearable assistive technology designed to bridge the communication gap between sign language users and non-signers. The system captures finger movements and hand orientation using embedded sensors, streams data wirelessly via MQTT, and uses machine learning models to translate sign language gestures into text and speech in real time.

---

# Hardware Stack

## Core Processing Unit

### ESP32 DevKit V1

**Purpose:**

* Reads sensor data
* Connects to Wi-Fi
* Publishes MQTT messages
* Handles real-time communication

---

## Gesture Recognition Sensors

### Flex Sensors (5x)

Mounted on:

* Thumb
* Index Finger
* Middle Finger
* Ring Finger
* Pinky Finger

**Purpose:**

* Detect finger bending angles
* Capture hand shapes
* Recognize alphabets and static gestures

---

### MPU6050 IMU Sensor

Contains:

* 3-Axis Accelerometer
* 3-Axis Gyroscope

**Purpose:**

* Measure hand movement
* Detect gesture trajectories
* Capture orientation and motion dynamics

---

## User Interface Components

### Push Button

**Purpose:**

* Start/stop dataset recording
* Switch operating modes
* Calibration trigger

---

### Speaker / Bluetooth Earbuds

**Purpose:**

* Convert recognized text into speech output

---

## Power System

### Power Options

* 3.7V Li-ion Battery
* 5V Power Bank

**Purpose:**

* Portable operation
* Long battery backup

---

# Communication Stack

## MQTT Protocol

### MQTT Broker

Mosquitto Broker

**Purpose:**

* Receives sensor data from ESP32
* Distributes data to machine learning applications

### MQTT Topic Structure

```text
glovetalk/sensors
glovetalk/predictions
glovetalk/status
```

---

# Software Stack

## Embedded Software

### Development Environment

```text
Arduino IDE
```

### Libraries

```cpp
WiFi.h
PubSubClient.h
Wire.h
Adafruit_MPU6050.h
ArduinoJson.h
```

---

## Data Collection Layer

### Language

```text
Python
```

### Libraries

```python
numpy
pandas
paho-mqtt
csv
```

**Purpose:**

* Receive MQTT packets
* Store labeled gesture datasets
* Create training samples

---

## Machine Learning Layer

### Phase 1: Baseline Models

Algorithms:

* Random Forest
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

Libraries:

```python
scikit-learn
joblib
```

---

### Phase 2: Deep Learning

Algorithm:

```text
LSTM (Long Short-Term Memory)
```

Libraries:

```python
TensorFlow
Keras
NumPy
```

**Purpose:**

* Learn temporal gesture patterns
* Recognize dynamic sign language words
* Support continuous gesture sequences

---

## Speech Generation Layer

### Offline TTS

```python
pyttsx3
```

### Online TTS

```python
gTTS
```

**Purpose:**

Convert predicted text into natural speech.

---

## Visualization & Debugging

### MQTT Explorer

Used for:

* Monitoring MQTT topics
* Debugging sensor packets
* Verifying communication

### Node-RED (Optional)

Used for:

* Dashboards
* Real-time monitoring
* System analytics

---

# AI Pipeline

```text
Flex Sensors (5)
        +
     MPU6050
        |
        v
      ESP32
        |
        v
      Wi-Fi
        |
        v
   MQTT Broker
   (Mosquitto)
        |
        v
 Python Subscriber
        |
        v
 Feature Extraction
        |
        v
 Random Forest / LSTM
        |
        v
 Predicted Word
        |
        v
 Text Output
        |
        v
 Speech Output
```

---

# Dataset Structure

```text
dataset/
│
├── hello/
│   ├── sample_1.csv
│   ├── sample_2.csv
│   └── sample_3.csv
│
├── thank_you/
│   ├── sample_1.csv
│   └── sample_2.csv
│
├── yes/
├── no/
├── water/
└── help/
```

Each sample contains:

```text
40 Time Steps × 11 Features
```

Features:

```text
Flex1
Flex2
Flex3
Flex4
Flex5
AccX
AccY
AccZ
GyroX
GyroY
GyroZ
```

---

# Future Enhancements

## Computer Vision Integration

Additional Hardware:

* Camera Module

Additional Software:

* MediaPipe Hands
* YOLO

Benefits:

* Improved recognition accuracy
* Body-relative gesture detection
* Continuous sentence translation

---

# Bill of Materials (BOM)

| Component                    | Quantity |
| ---------------------------- | -------- |
| ESP32 DevKit V1              | 1        |
| Flex Sensor                  | 5        |
| MPU6050                      | 1        |
| Push Button                  | 1        |
| Battery / Power Bank         | 1        |
| Resistors (Voltage Dividers) | 5        |
| Smart Glove                  | 1        |
| Laptop                       | 1        |
| Mosquitto MQTT Broker        | 1        |

---

# Target Features

* Real-Time Sign Language Recognition
* Wireless MQTT Communication
* AI-Based Gesture Classification
* Text Generation
* Speech Generation
* Dataset Collection Framework
* Expandable Vocabulary
* Future Continuous Sentence Recognition

---
