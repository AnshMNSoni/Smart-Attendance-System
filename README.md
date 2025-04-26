# Smart Attendance System

### 📑 Project Overview
This project demonstrates a simple RFID Attendance System using an Arduino UNO, RFID-RC522 module, and a 16x2 LCD (I2C Interface).
The system reads RFID cards and displays the user information or attendance status on the LCD screen.

### 📦 Components Used
- Arduino UNO

- RFID-RC522 Module

- LCD 16x2 with I2C Adapter

- Jumper Wires

- Breadboard (optional)

- RFID Tags/Cards

### 🛠️ Working Principle
- When a valid RFID card/tag is brought near the RFID reader

- The system reads the unique ID (UID) of the card.

- It displays the UId, date and time.

### 🖥️ Libraries Required
Make sure to install the following libraries in Arduino IDE:

- MFRC522 (for RFID module communication)

- Wire.h (for I2C communication)

- LiquidCrystal_I2C (for LCD 16x2)

📌 You can install them through Arduino Library Manager.

🧩 Code Structure (Brief Overview)
Initialization: Setup LCD and RFID module.

Loop: Continuously check for a card presence.

UID: Scanned UID using RFID Reader.

Display Messages: Print appropriate messages on LCD.

### 📸 Project Pin Diagram

![Screenshot 2025-04-26 102613](https://github.com/user-attachments/assets/f625483b-c0ef-415b-b01a-ecfc2e8929e4)

### 📸 Original Connection Diagram

![IoT-Project-SS](https://github.com/user-attachments/assets/53c50adb-9007-4051-91c4-5911b04ff698)

### 📸 Website Look

![Screenshot (56)](https://github.com/user-attachments/assets/afd01674-32b7-41a7-ae15-c469d4a730e2)


### ⚡ Future Improvements
- Store multiple users in EEPROM.

- Add a Real-Time Clock (RTC) module to record timestamps.

- Send attendance data to a computer or cloud service via Wi-Fi module.

- Buzzer or LED indicators for feedback.

### 🙌 Acknowledgments
#### Thanks to
- Team Members: Maitree Mistry, Jenil Savaliya and Rudra Joshi
- Open-source community and documentation resources that made this project possible.

### 📬 Contact
For any queries, feel free to reach out!

# 🚀 Happy Building!
