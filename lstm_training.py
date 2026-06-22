import paho.mqtt.client as mqtt
import time
import os
import csv

# --- CONFIGURATION ---
MQTT_BROKER = "192.168.1.X" # Use the exact same broker IP/address as the ESP32
MQTT_TOPIC = "glove/sensors"
TIME_STEPS = 40
DATA_FOLDER = "sign_dataset"

# Global variables to handle incoming data stream
latest_data = None

def on_message(client, userdata, msg):
    global latest_data
    # Decode the incoming payload string
    latest_data = msg.payload.decode('utf-8')

# Set up MQTT Subscriber Client
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start() # Start background thread to listen for data

print("--- Wireless MQTT Sign Language Data Collector ---")

while True:
    word = input("\nEnter the word you want to sign (or type 'exit' to quit): ").strip().lower()
    if word == 'exit': break
        
    word_folder = os.path.join(DATA_FOLDER, word)
    os.makedirs(word_folder, exist_ok=True)
    
    sample_num = len([f for f in os.listdir(word_folder) if f.endswith('.csv')]) + 1
    file_path = os.path.join(word_folder, f"sample_{sample_num}.csv")
    
    print("Get ready...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("START SIGNING NOW!")
    
    latest_data = None # Clear old frame
    recorded_rows = []
    
    while len(recorded_rows) < TIME_STEPS:
        if latest_data is not None:
            data_points = latest_data.split(',')
            if len(data_points) == 11:
                recorded_rows.append(data_points)
            latest_data = None # Reset to wait for the next unique MQTT message
            time.sleep(0.04) # Match the ~50ms frequency of the ESP32
                
    with open(file_path, 'w', newline='') as f:
        csv.writer(f).writerows(recorded_rows)
        
    print(f"✔️ Saved: {file_path}")

client.loop_stop()
