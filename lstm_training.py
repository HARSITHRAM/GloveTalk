import serial
import time
import os
import csv

# --- CONFIGURATION ---
# Change 'COM3' to your actual port (e.g., '/dev/ttyUSB0' on Linux/Mac)
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600
TIME_STEPS = 40        # Number of data rows per gesture (e.g., 2 seconds at 20Hz)
DATA_FOLDER = "sign_dataset"

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2) # Wait for connection to stabilize

print("--- Sign Language Data Collector Initialized ---")

while True:
    # Step 1: Ask the user what word they want to train
    word = input("\nEnter the word you want to sign (or type 'exit' to quit): ").strip().lower()
    
    if word == 'exit':
        break
        
    # Step 2: Create a specific folder for that word if it doesn't exist
    word_folder = os.path.join(DATA_FOLDER, word)
    os.makedirs(word_folder, exist_ok=True)
    
    # Count existing files to name the next sample correctly (e.g., sample_1.csv, sample_2.csv)
    existing_samples = len([f for f in os.listdir(word_folder) if f.endswith('.csv')])
    sample_num = existing_samples + 1
    file_path = os.path.join(word_folder, f"sample_{sample_num}.csv")
    
    # Step 3: Countdown so you can get your hand ready
    print("Get ready...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("START SIGNING NOW!")
    
    # Flush old data in the serial buffer so we only get the fresh movement
    ser.reset_input_buffer()
    
    # Step 4: Record the fixed number of time steps
    recorded_rows = []
    while len(recorded_rows) < TIME_STEPS:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            # Split the string by commas into a list of numbers
            data_points = line.split(',')
            
            # Basic check to ensure we got all 11 sensor values
            if len(data_points) == 11:
                recorded_rows.append(data_points)
                
    # Step 5: Save the recorded matrix to a CSV file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(recorded_rows)
        
    print(f"✔️ Saved: {file_path} ({TIME_STEPS} rows recorded)")

ser.close()
print("Data collection finished.")
