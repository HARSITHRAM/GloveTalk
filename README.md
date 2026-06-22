# GloveTalk
This Project combines embedded and LSTM to convert sign language to actual sentences  

# SignSync: An LSTM-Powered Smart Glove for Sign Language Translation

SignSync is an assistive technology wearable designed to bridge the communication gap between the deaf community and the hearing world. By combining hardware sensor arrays with Deep Learning, this smart glove translates continuous hand gestures and finger movements into digital text and speech in real-time.

---

## 🚀 Key Features
- **Continuous Gesture Recognition:** Tracks fluid, time-dependent signs (not just static letters) using sequence modeling.
- **Dual-Sensor Array:** Uses physical flex sensors for finger bending alongside an Inertial Measurement Unit (IMU) for 3D hand trajectory.
- **Edge-Ready Architecture:** Designed to capture raw data efficiently and deploy via lightweight neural networks.

---

## 🛠️ System Architecture

The project splits functionality across hardware data collection and software sequence prediction:

### 1. Hardware Array
- **5x Flex Sensors:** Positioned on each finger to capture individual joint angles and static hand shapes.
- **1x MPU6050 (Gyroscope + Accelerometer):** Captures dynamic data including 3-axis acceleration, rotational speed, and hand orientation.
- **Microcontroller:** Reads analog/I2C signals and streams packetized data over Serial at a fixed frame rate (20Hz).

### 2. Deep Learning Pipeline (LSTM)
Unlike standard classification models, this project uses a **Long Short-Term Memory (LSTM)** network. LSTMs introduce a temporal feedback loop ("memory"), making them uniquely capable of:
- Processing time-series sensor data windows.
- Handling variable signing speeds (time-invariance).
- Tracking contextual hand trajectories over a 2-second moving window.

---

## 📁 Repository Structure

```text
├── hardware/
│   └── glove_firmware.ino     # Microcontroller code to stream sensor data
├── ml_model/
│   ├── data_collector.py      # Method 1: Hotkey-prompt dataset script
│   ├── lstm_training.py          # TensorFlow/Keras training pipeline
│   └── sign_sync_model.h5     # Trained LSTM weights file
├── sign_dataset/              # Collected samples split by gesture label
│   ├── hello/
│   └── thank_you/
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- Arduino IDE (or PlatformIO)

### Python Dependencies
Install the required machine learning and utility libraries:
```bash
pip install tensorflow numpy pyserial csv-validators
```

---

## 📈 How It Works

### Step 1: Data Collection
1. Connect your smart glove to your computer via USB.
2. Run the `data_collector.py` script.
3. Input the word label you wish to sign when prompted.
4. Complete the gesture during the 3-second countdown. The script logs a fixed frame window matrix (e.g., 40 time steps × 11 sensor channels) directly into a labeled CSV.

### Step 2: Training the Model
Run the training script to feed the sequence matrices into the LSTM network:
```bash
python ml_model/train_lstm.py
```
The model utilizes dropout layers to prevent overfitting and a softmax activation layer to yield word probability scores.

---

## 👥 Authors
- **HARSITHRAM** - *Lead Developer* - [@HARSITHRAM](https://github.com/HARSITHRAM/)

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

