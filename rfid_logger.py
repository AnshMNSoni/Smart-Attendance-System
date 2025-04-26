import serial
import csv
from datetime import datetime
import os

try:
    arduino = serial.Serial('COM6', 9600, timeout=1)
    print("Connected to Arduino... Logging started.")
except serial.SerialException as e:
    print(f"Failed to connect: {e}")
    exit()

csv_file = 'rfid_log.csv'

# Check if CSV file exists and has headers
file_exists = os.path.exists(csv_file)
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists or os.stat(csv_file).st_size == 0:
        writer.writerow(['UID', 'Date', 'Time'])

    try:
        while True:
            line = arduino.readline().decode('utf-8').strip()   
            if line.startswith("UID:"):
                uid = line.split("UID: ")[1].strip()
                now = datetime.now()
                date = now.strftime('%Y-%m-%d')
                time = now.strftime('%H:%M:%S')
                writer.writerow([uid, date, time])
                file.flush()  # Write immediately
                print(f"Logged: {uid} at {time} on {date}")
    except KeyboardInterrupt:
        print("Logging stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
